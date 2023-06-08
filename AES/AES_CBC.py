# -*- coding: utf-8 -*-
# @date：2022/12/20 9:20
# @Author：crab-pc
# @file： python_AES
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

iv = '0000000000000000'
key = '7E79g12u3i4d5e68'


# 将明文用AES加密
def AES_en(key, data):
    padtext = pad(data, 16, style='pkcs7')
    # 创建加密对象
    AES_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成加密
    AES_en_str = AES_obj.encrypt(padtext)
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str


# 解密
def AES_de(key, data):
    # 解密过程逆着加密过程写
    # 将密文字符串重新编码成二进制形式
    data = data.encode("utf-8")
    # 将base64的编码解开
    data = base64.b64decode(data)
    # 创建解密对象
    AES_de_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成解密
    AES_de_str = AES_de_obj.decrypt(data)
    # 去掉补上的空格
    AES_de_str = AES_de_str.strip()
    # 对明文解码
    AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str


data = '123456'.encode('utf-8')
data = AES_en(key, data)
print(data)
data = AES_de(key, data)
print(data)
