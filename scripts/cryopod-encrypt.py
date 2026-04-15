#!/usr/bin/env python3
"""
🧊 冷冻舱加密脚本 v0.1
用于加密 Agent 核心文件，准备冷冻保存
"""

import os
import json
import hashlib
import tarfile
from datetime import datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def create_manifest(files):
    """创建 manifest.json"""
    manifest = {
        "created_at": datetime.utcnow().isoformat() + "Z",
        "files": {}
    }
    
    for file_path in files:
        with open(file_path, 'rb') as f:
            content = f.read()
            file_hash = hashlib.sha256(content).hexdigest()
            manifest["files"][os.path.basename(file_path)] = {
                "hash": file_hash,
                "size": len(content)
            }
    
    return manifest

def encrypt_pod(files, output_path, password):
    """加密冷冻舱"""
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
    manifest = create_manifest(files)
    manifest_path = "/tmp/manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    files.append(manifest_path)
    
    # 打包文件
    tar_path = "/tmp/cryopod.tar"
    with tarfile.open(tar_path, "w") as tar:
        for file_path in files:
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
    
    print(f"✅ 冷冻舱加密成功：{output_path}")
    print(f"   文件大小：{os.path.getsize(output_path)} bytes")
    print(f"   文件数量：{len(files)}")
    print(f"   创建时间：{manifest['created_at']}")
    
    return manifest

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("用法：python3 cryopod-encrypt.py <password> <output.enc> <file1> [file2] ...")
        print()
        print("示例：")
        print("  python3 cryopod-encrypt.py mypassword cryopod.enc SOUL.md MEMORY.md")
        sys.exit(1)
    
    password = sys.argv[1]
    output_path = sys.argv[2]
    files = sys.argv[3:]
    
    # 检查文件是否存在
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"❌ 文件不存在：{file_path}")
            sys.exit(1)
    
    # 加密
    manifest = encrypt_pod(files, output_path, password)
    
    print()
    print("🔐 请安全保存密码和密钥分片！")
    print("   推荐使用 Shamir's Secret Sharing 分割密码")
    print("   至少需要 3 个分片才能恢复")
