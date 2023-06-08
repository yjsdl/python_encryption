# -*- coding: utf-8 -*-
# @date：2023/5/26 17:10
# @Author：LiuYiJie
# @file： pbk_encrypto
"""
PBKDF2 将伪随机函数（例如 HMAC），把明文和一个盐值（salt）作为输入参数，然后进行重复运算，并最终产生密钥
"""
import binascii
from Crypto.Hash import SHA1
from Crypto.Protocol.KDF import PBKDF2


def PbkEncrypto(text):
    salt = b'43215678'
    res = PBKDF2(text, salt, count=10, hmac_hash_module=SHA1)
    result = binascii.hexlify(res)
    return result.decode('utf-8')


text = '123456'
result = PbkEncrypto(text)
print(result)
