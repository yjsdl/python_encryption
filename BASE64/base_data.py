# -*- coding: utf-8 -*-
# @date：2023/5/18 17:48
# @Author：LiuYiJie
# @file： base_data
import base64


def baseEncrypt(data):
    con = data.encode(encoding='utf-8')
    result = base64.b64encode(con)
    return result


if __name__ == '__main__':
    data = '123456'
    result = baseEncrypt(data)
    print(result)
