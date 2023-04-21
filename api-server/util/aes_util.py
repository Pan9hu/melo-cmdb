from Crypto.Cipher import AES


class AESUtil:
    """
    aes加密算法
    padding : PKCS7
    """
    __key = b"8678f6b7bf2547b5aacd4f68074f6e2c"  # 32位
    __iv = b"2752084042949672"  # 16位
    __BLOCK_SIZE_16 = BLOCK_SIZE_16 = AES.block_size

    @staticmethod
    def encrypt(content: str):
        """
        加密文本
        :param content: 文本
        :return: 密文
        """
        cipher = AES.new(AESUtil.__key, AES.MODE_CBC, AESUtil.__iv)
        x = AESUtil.__BLOCK_SIZE_16 - (len(content) % AESUtil.__BLOCK_SIZE_16)
        # 如果最后一块不够16位需要用字符进行补全
        if x != 0:
            content = content + chr(x) * x
        msg = cipher.encrypt(content.encode('utf-8'))
        return msg

    @staticmethod
    def decrypt(en_str):
        cipher = AES.new(AESUtil.__key, AES.MODE_CBC, AESUtil.__iv)
        msg = cipher.decrypt(en_str)
        padding_len = msg[len(msg) - 1]
        return msg[0:-padding_len]
