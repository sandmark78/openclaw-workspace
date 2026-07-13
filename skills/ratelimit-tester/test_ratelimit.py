#!/usr/bin/env python3
"""
ratelimit-tester — 百炼/DashScope 模型速率限制测试
测试 qwen3.6-plus 通过 coding.dashscope.aliyuncs.com 的 RPM/并发/token 限制
"""
import urllib.request, urllib.error, json, time, sys, os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Config
API_KEY = os.getenv("BAILIAN_API_KEY", "sk-sp-3a3cc83013574bffbbfb707615433d95")
BASE_URL = "https://coding.dashscope.aliyuncs.com/v1/chat/completions"
MODEL = "qwen3.6-plus"
TIMEOUT = 120  # seconds per request

def chat_completion(req_id, prompt="Say OK.", max_tokens=10, timeout=TIMEOUT):
    """Make a single chat completion request"""
    start = time.time()
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens
    }).encode('utf-8')
    
    req = urllib.request.Request(BASE_URL, data=payload, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            elapsed = time.time() - start
            data = json.loads(resp.read())
            usage = data.get("usage", {})
            return {
                "id": req_id,
                "status": resp.status,
                "elapsed": round(elapsed, 2),
                "prompt_tokens": usage.get("prompt_tokens", 0),
                "completion_tokens": usage.get("completion_tokens", 0),
                "total_tokens": usage.get("total_tokens", 0),
            }
    except urllib.error.HTTPError as e:
        elapsed = time.time() - start
        body = e.read().decode('utf-8', errors='ignore')[:300]
        return {
            "id": req_id, "status": e.code,
            "elapsed": round(elapsed, 2), "body": body,
            "headers": dict(e.headers)
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "id": req_id, "status": "ERR",
            "elapsed": round(elapsed, 2), "error": str(e)[:300]
        }

def parse_rate_limit(headers):
    """Extract rate limit info from response headers"""
    if not headers:
        return {}
    info = {}
    for key in ['x-ratelimit-limit-requests', 'x-ratelimit-remaining-requests',
                'x-ratelimit-limit-tokens', 'x-ratelimit-remaining-tokens',
                'retry-after']:
        val = headers.get(key) or headers.get(key.title()) or headers.get(key.lower())
        if val:
            info[key] = val
    return info

def print_result(r, verbose=False):
    if r["status"] == 200:
        print(f"  ✅ {r['id']}: {r['elapsed']}s, {r['total_tokens']} tokens "
              f"(prompt={r['prompt_tokens']}, completion={r['completion_tokens']})")
    else:
        status = r.get('status', '???')
        body = r.get('body', r.get('error', ''))[:150]
        rl_info = parse_rate_limit(r.get('headers', {}))
        print(f"  ❌ {r['id']}: HTTP {status} ({r['elapsed']}s)")
        if rl_info:
            print(f"     Rate Limit Headers: {rl_info}")
        if verbose:
            print(f"     Body: {body}")

def test_single():
    """Test 1: Single call baseline"""
    print("\n" + "=" * 70)
    print("TEST 1: 单次调用基线测试")
    print("=" * 70)
    r = chat_completion("baseline-1", "Explain quantum computing in 20 words.", max_tokens=50)
    print_result(r, verbose=True)
    return r

def test_sequential():
    """Test 2: Sequential calls"""
    print("\n" + "=" * 70)
    print("TEST 2: 连续调用上限测试")
    print("=" * 70)
    
    ok = 0
    total_tokens = 0
    total_time = 0
    results = []
    
    for i in range(30):
        r = chat_completion(f"seq-{i+1}", "Say hello.", max_tokens=5)
        results.append(r)
        if r["status"] == 200:
            ok += 1
            total_tokens += r.get("total_tokens", 0)
            total_time += r["elapsed"]
            print_result(r)
        else:
            print_result(r, verbose=True)
            # Retry once after 60s
            print(f"  ⏳ 等待 60 秒后重试...")
            time.sleep(60)
            r2 = chat_completion(f"seq-{i+1}-retry", "Say hello.", max_tokens=5)
            if r2["status"] == 200:
                ok += 1
                total_tokens += r2.get("total_tokens", 0)
                total_time += r2["elapsed"]
                print_result(r2)
                print(f"  ✅ 重试成功")
            else:
                print(f"  ❌ 重试也失败: {r2.get('status')} - {r2.get('body', r2.get('error',''))[:100]}")
                break
    
    print(f"\n  结果: {ok}/30 成功")
    if ok > 0:
        print(f"  平均响应时间: {total_time/ok:.2f}s")
        print(f"  平均 token 消耗: {total_tokens/ok:.0f} tokens/调用")
        print(f"  总 token 消耗: {total_tokens}")
    return ok

def test_concurrent():
    """Test 3: Concurrent calls"""
    print("\n" + "=" * 70)
    print("TEST 3: 并发调用上限测试")
    print("=" * 70)
    
    # Warm up
    print("  🔥 预热 1 次...")
    warmup = chat_completion("warmup", "Hi.", max_tokens=5)
    
    for n in [2, 5, 10, 15, 20, 30, 50]:
        print(f"\n  测试 {n} 路并发...")
        results = []
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=n) as ex:
            futures = [ex.submit(chat_completion, f"con{n}-{i+1}", "Say OK.", max_tokens=5) 
                       for i in range(n)]
            for f in as_completed(futures):
                results.append(f.result())
        total_time = time.time() - start_time
        
        ok = sum(1 for r in results if r["status"] == 200)
        fails = [r for r in results if r["status"] != 200]
        total_tokens = sum(r.get("total_tokens", 0) for r in results if r["status"] == 200)
        
        print(f"    ✅ 成功: {ok}/{n}")
        if ok < n:
            for r in fails[:3]:
                print_result(r, verbose=True)
            if len(fails) > 3:
                print(f"    ... 还有 {len(fails)-3} 个失败")
        
        # Check rate limit headers
        rl_headers = set()
        for r in results:
            if r["status"] == 200:
                rl = parse_rate_limit(r.get('headers', {}))
                if rl:
                    rl_headers.add(json.dumps(rl, sort_keys=True))
        if rl_headers:
            print(f"    📊 Rate Limit Headers: {list(rl_headers)[:2]}")
        
        print(f"    ⏱️ 总耗时: {total_time:.2f}s")
        print(f"    🔢 总 token: {total_tokens}")
        
        if ok < n:
            print(f"\n  ⚠️ 并发限制在 {n} 附近！")
            break
        
        # Wait between tests
        if ok == n and n < 50:
            print(f"    等待 30 秒冷却...")
            time.sleep(30)
    
    return ok

def test_token_limit():
    """Test 4: Token consumption rate"""
    print("\n" + "=" * 70)
    print("TEST 4: Token 消耗速率测试")
    print("=" * 70)
    
    # Make 5 calls with moderate output
    print("  发送 5 次中等长度请求...")
    results = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = [ex.submit(chat_completion, f"tok-{i+1}", 
                           "Write a 200-word essay about AI agents.", max_tokens=300) 
                   for i in range(5)]
        for f in as_completed(futures):
            results.append(f.result())
    
    ok = sum(1 for r in results if r["status"] == 200)
    total_tokens = sum(r.get("total_tokens", 0) for r in results if r["status"] == 200)
    
    print(f"  ✅ {ok}/5 成功")
    print(f"  🔢 总 token: {total_tokens}")
    for r in results:
        if r["status"] == 200:
            print_result(r)
        else:
            print_result(r, verbose=True)
    
    return total_tokens

def main():
    print("🔬 Rate Limit Tester — 百炼 qwen3.6-plus 速率限制测试")
    print(f"   API: {BASE_URL}")
    print(f"   Model: {MODEL}")
    print(f"   Timeout: {TIMEOUT}s")
    
    # Test 1: Baseline
    baseline = test_single()
    if baseline["status"] != 200:
        print("\n❌ 基线测试失败，无法继续。请检查 API Key 和网络。")
        sys.exit(1)
    
    print("\n✅ 基线测试通过，继续...")
    
    # Test 2: Sequential
    seq_ok = test_sequential()
    
    # Wait between tests
    print("\n  ⏳ 等待 60 秒冷却...")
    time.sleep(60)
    
    # Test 3: Concurrent
    con_ok = test_concurrent()
    
    # Wait between tests
    print("\n  ⏳ 等待 60 秒冷却...")
    time.sleep(60)
    
    # Test 4: Token limit
    tok_total = test_token_limit()
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 测试总结")
    print("=" * 70)
    print(f"  单次调用: {baseline['elapsed']}s, {baseline['total_tokens']} tokens")
    print(f"  连续调用: {seq_ok}/30 成功")
    print(f"  并发测试: 最高 {con_ok} 路并发成功")
    print(f"  Token 消耗: {tok_total} tokens (5 次调用)")
    print("=" * 70)

if __name__ == "__main__":
    main()
