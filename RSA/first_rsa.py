# -*- coding: utf-8 -*-
# @date：2023/5/18 17:17
# @Author：LiuYiJie
# @file： first_rsa
import rsa


def rsaEncrypt(data, pubkey):
    # 生成公钥、私钥
    data = data.encode(encoding='utf-8')
    # 公钥加密
    result = rsa.encrypt(data, pubkey)
    return result


def rsaDecrypt(data, privkey):
    data = rsa.decrypt(data, privkey)
    data = data.decode(encoding='utf-8')
    return data


if __name__ == '__main__':
    pubkey, privkey = rsa.newkeys(512)
    data = 'I love Python'
    result = rsaEncrypt(data, pubkey)
    print(result)
    result = rsaDecrypt(result, privkey)
    print(result)
