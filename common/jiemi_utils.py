"""
Author: lihao
Time: 2022/6/6

"""
import base64
import json

from Crypto.Cipher import AES


def decrypt(decrData, password):
    """
    解密数据
    :param decrData: 解密正文
    :param password: 密钥
    :return: 解密结果
    """
    if isinstance(password, str):
        password = password.encode('utf8')
    aes = AES.new(password, AES.MODE_ECB)
    en_text = decrData.encode()
    en_text = base64.decodebytes(en_text)
    den_text = aes.decrypt(en_text)
    return den_text.decode("utf8")



