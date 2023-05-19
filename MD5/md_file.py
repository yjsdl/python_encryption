# -*- coding: utf-8 -*-
# @date：2023/5/18 16:00
# @Author：LiuYiJie
# @file： md_file

import io
import hashlib


def md_encryption(data):
    res = hashlib.md5()
    data = data.encode(encoding='utf-8')
    res.update(data)
    result = res.hexdigest()
    return result


if __name__ == '__main__':
    print(md_encryption('123456'))
