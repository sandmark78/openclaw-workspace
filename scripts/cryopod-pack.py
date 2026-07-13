#!/usr/bin/env python3
"""
🧊 冷冻舱打包脚本 v0.1
一键生成加密冷冻包 + 清单
"""

import os
import json
import hashlib
import tarfile
import argparse
from datetime import datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def create_manifest(files, metadata):
    """创建 manifest.json"""
    manifest = {
        "schema_version": "1.0",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "agent": metadata,
        "files": {}
    }
    
    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                file_hash = hashlib.sha256(content).hexdigest()
                manifest["files"][os.path.basename(file_path)] = {
                    "hash": file_hash,
                    "size": len(content)
                }
    
    return manifest

def encrypt_pod(files, output_path, password, metadata={}):
    """加密冷冻舱"""
    print(f"🧊 开始创建冷冻舱...")
    print(f"   输出文件：{output_path}")
    print(f"   文件数量：{len(files)}")
    
    # 生成盐值和密钥
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    
    # 创建 manifest
    manifest = create_manifest(files, metadata)
    manifest_path = "/tmp/manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    files.append(manifest_path)
    
    # 打包文件
    tar_path = "/tmp/cryopod.tar"
    with tarfile.open(tar_path, "w") as tar:
        for file_path in files:
            if os.path.exists(file_path):
                tar.add(file_path, arcname=os.path.basename(file_path))
    
    # 读取 tar 数据
    with open(tar_path, 'rb') as f:
        tar_data = f.read()
    
    # 加密
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, tar_data, None)
    
    # 保存加密文件
    with open(output_path, 'wb') as f:
        f.write(salt + nonce + ciphertext)
    
    # 清理临时文件
    os.remove(tar_path)
    os.remove(manifest_path)
    
    # 输出信息
    print()
    print(f"✅ 冷冻舱创建成功！")
    print(f"   文件大小：{os.path.getsize(output_path):,} bytes")
    print(f"   加密算法：AES-256-GCM")
    print(f"   密钥派生：PBKDF2-SHA256 (100000 次)")
    print()
    print(f"📋 文件清单:")
    for filename, info in manifest["files"].items():
        print(f"   - {filename} ({info['size']:,} bytes, {info['hash'][:16]}...)")
    print()
    print(f"🔐 请安全保存密码！")
    print(f"   推荐使用 Shamir's Secret Sharing 分割密码")
    print(f"   至少需要 3 个分片才能恢复")
    
    return manifest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🧊 冷冻舱打包脚本 v0.1")
    parser.add_argument("password", help="加密密码")
    parser.add_argument("output", help="输出文件路径 (.enc)")
    parser.add_argument("files", nargs="+", help="要打包的文件")
    parser.add_argument("--name", default="sandbot-lobster", help="Agent 名称")
    parser.add_argument("--version", default="V6.3", help="Agent 版本")
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    missing = [f for f in args.files if not os.path.exists(f)]
    if missing:
        print(f"❌ 文件不存在：{missing}")
        exit(1)
    
    # 元数据
    metadata = {
        "name": args.name,
        "version": args.version,
        "framework": "OpenClaw V6.3"
    }
    
    # 加密
    manifest = encrypt_pod(args.files, args.output, args.password, metadata)
