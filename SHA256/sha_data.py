# -*- coding: utf-8 -*-
# @date：2023/5/18 17:29
# @Author：LiuYiJie
# @file： sha256
import hashlib


def shaEncrypt(data):
    sha = hashlib.sha256()
    data = data.encode(encoding='utf-8')
    sha.update(data)
    result = sha.hexdigest()
    return result


if __name__ == '__main__':
    data = '123456'
    result = shaEncrypt(data)
    print(result)