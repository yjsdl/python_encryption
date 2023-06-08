# -*- coding: utf-8 -*-
# @date：2023/5/18 16:00
# @Author：LiuYiJie
# @file： md_file
"""
简介：全称 MD5 消息摘要算法（英文名称：MD5 Message-Digest Algorithm），又称哈希算法、散列算法，由美国密码学家罗纳德·李维斯特（Ronald Linn Rivest）设计，于 1992 年作为 RFC 1321 被公布，用以取代 MD4 算法。摘要算法是单向加密的，也就是说明文通过摘要算法加密之后，是不能解密的。摘要算法的第二个特点密文是固定长度的，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。之所以叫摘要算法，它的算法就是提取明文重要的特征。所以，两个不同的明文，使用了摘要算法之后，有可能他们的密文是一样的，不过这个概率非常的低。
"""

import io
import hashlib


def md_encryption1(data):
    data = data.encode(encoding='utf-8')
    res = hashlib.new('md5', data)
    result = res.hexdigest()
    return result


def md_encryption(data):
    res = hashlib.md5()
    data = data.encode(encoding='utf-8')
    res.update(data)
    # res.update('123'.encode('utf-8'))
    # res.update('456'.encode('utf-8'))
    result = res.hexdigest()
    return result


if __name__ == '__main__':
    data = '123456'
    print(md_encryption1(data))
    print(md_encryption(data))
