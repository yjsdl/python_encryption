# -*- coding: utf-8 -*-
# @date：2023/6/7 17:03
# @Author：LiuYiJie
# @file： hamc
import hmac


def hmac_test1(text):
    key = '123456'.encode('utf-8')
    text = text.encode('utf-8')
    md5 = hmac.new(key, text, digestmod="MD5")
    result = md5.hexdigest()
    return result


def hmac_test2(text):
    key = '123456'.encode('utf-8')
    text = text.encode('utf-8')
    sha1 = hmac.new(key, digestmod='sha1')
    sha1.update(text)
    result = sha1.hexdigest()
    return result


if __name__ == '__main__':
    text = '123456'
    print(hmac_test1(text))
    print(hmac_test2(text))
