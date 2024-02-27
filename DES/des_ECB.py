# -*- coding: utf-8 -*-
# @date：2024/2/27 14:45
# @Author：LiuYiJie
# @file： des_ECB
import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


class DESCrypt:
    def __init__(self, key, mode):
        self.key = key  # 密钥
        self.mode = mode  # 模式

    def encrpyt(self, text):
        '''加密'''

        text_pad = text.encode('utf-8')  # 填充后的字节串
        # 补全缺失长度，必须是8的倍数
        padded_data = pad(text_pad, DES.block_size)
        cipher = DES.new(self.key, self.mode)
        encrypt_data = cipher.encrypt(padded_data)  # 对数据进行加密
        result = base64.b64encode(encrypt_data).decode()
        return result

    def decrypt(self, text):
        '''解密'''

        data = base64.b64decode(text.encode())
        crpytor = DES.new(self.key, self.mode)
        decrypt_data = crpytor.decrypt(data)  # 对数据进行解密
        res = decrypt_data[:-decrypt_data[-1]].decode()  # 去除多余字符
        return res


if __name__ == '__main__':
    # key = random._urandom(8) 可以利用random模块随机生成
    # key = b'C\xc5\xa0\x04!\xe3\xd59'  # 密钥,固定8个字节长度
    key = b'WhoAmIOO'  # 密钥,固定8个字节长度
    mode = DES.MODE_ECB
    des = DESCrypt(key, mode)

    text = '/GHYtbSWprABRoBEH6vFq17ri9AewLjYSYBUfMxYHNdgnZ+aHCr0p7oh3LdEF6u7rzL9iG2d/k6RJOtnRaxhcbDkbmCOOAln4/3 ZPsEJ5cztSulJvmARPqVhvuHNYRh6jjltXMxMil3M7opQI8Caf/PV1ygLnKIXRDEE8X1h4ehP/gUBshmDeMh/5 j+NgWCtPpGu4hdgTaT1L4+X7vcBI3NCWm5OOTMkHdYgEs8g0eCcIt+lHnNN8jle9oJYYEK/7 oq2hsPZ/s5kt+LVtT7iJLOCvBgsm9LDQDiZizYjitWFKnf4gBnD/DNA2QPx4cxOI2eSFua7btvlHnE1+o96k16Lt9Dl4u+M+P2Ytyf4z80ESbnyheWTV5zQTSpTDdbb8m7AQD/zPHECPKK36UC85Ddrz5NPRfwIjl88139J+U7NzCezIzxYWpDOgA/WrYF+li7LpJk9/vHF8GuoGM6Y24UYDPe4d0UJw4TD799K51UcBLh9tqovxjXgaaNXGioNyYhLqZFHYK7PHxVBwXwHteCvqORW0okMi4Q8H7YmvduJsw3tYCcwvwkdesSnrxgLYy8LZdMgOzGd35XYficSWVL4JF77FlX8wc6Vidw49SFhHJrYqGocmCPCAube2fe3eAlD03Dn5sxZoRDnNm0V2owLfIJOIhbD9lLAKTi8AH7KJokyZgIpar696dzMfdKEfZZcnprtGQmsc7L1EEwl0AUKJfWsIoPLp9B+23 Q6/YiAaw9aPnDmBVjGT8Wliu0CjjRp86HjXZW5QBM/SmSE4iXUaNaRGftEhMPjRBQvB7a5V8g/eGzGJUgbwXFWgL7dvLKULQ0fah9Q/t2FxhZFJhIQ21eRZ33AKAAH/mhU2iTSYaLvVzF4rBkOpOyTjSBOoXnfCHS5Lcw+JWZBk+8 ZmGTxdI3XxdOQtIztALT/mtTxu4yMNexsveIoaJYRlz6RTuxF9/jfzpTuEfH6VKwz4ZqfhZF6U41fB6TgP3gcJZTkhmaRV687PNffUmQfcVCb+b+XIeux+0 XujpkV7YU1wg+0 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'
    de_data = des.decrypt(text)
    print('经过解密得到：%s' % de_data)
    en_data = des.encrpyt(de_data)
    print('经过加密得到：%s' % en_data)
    print(text == en_data)