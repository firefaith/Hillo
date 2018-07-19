# PyCrypto-based authenticated symetric encryption
# -*- coding: UTF-8 -*-
import hashlib
import hmac
import os
from Crypto.Cipher import AES
import string,random
from binascii import b2a_hex,a2b_hex
class AuthenticationError(Exception): pass

class Crypticle(object):
    """
    Authenticated encryption class
    Encryption algorithm: AES- [CBC,CFB,...]
    Signing algorithm: HMAC - [md5,sha256]
    """
    AES_BLOCK_SIZE = 16
    AES_KEY_SIZE = 16
    SIG_SIZE = hashlib.md5().digest_size # 16

    def __init__(self,aes_key=None,hmac_key=None,iv_key=None,hash_method="md5",aes_mode="CFB"): # 24*8,
        if aes_key is None:
            self.aes_key = self.generate_key(self.AES_KEY_SIZE)
        else:
            self.aes_key = aes_key
        if hmac_key is None:
            self.hmac_key = self.generate_key(self.SIG_SIZE)
        else:
            self.hmac_key = hmac_key

        if iv_key is None:
            self.iv_key = self.generate_key(self.AES_BLOCK_SIZE)
        else:
            self.iv_key = iv_key

        self.key_size = self.AES_KEY_SIZE * 8 #key_size
        self.aes_mode = getattr(AES,"MODE_{}".format(aes_mode.upper()))
        self.hash_method = getattr(hashlib,hash_method)
        self.SIG_SIZE = getattr(self.hash_method(),"digest_size")

    @classmethod
    def generate_key(cls,key_size=16): 
        str_set = string.ascii_letters + string.digits
        return ''.join(random.choice(str_set) for _ in range(key_size))


    def encrypt(self, data):
        """encrypt data with AES and sign it with HMAC"""
        cypher = AES.new(self.aes_key, self.aes_mode, self.iv_key)
        data = cypher.encrypt(data)
        sig = hmac.new(self.hmac_key, data, self.hash_method).digest() # default digestmod mod=md5
        return data + sig

    def decrypt(self, data):
        """verify HMAC signature and decrypt data with AES"""
        sig = data[-self.SIG_SIZE:]
        data = data[:-self.SIG_SIZE]
        if hmac.new(self.hmac_key, data, self.hash_method).digest() != sig:
            raise AuthenticationError("message authentication failed")
        cypher = AES.new(self.aes_key, self.aes_mode, self.iv_key)
        data = cypher.decrypt(data)
        return data



    def get_token(self,data): 
        """data as any object,like json or string etc."""
        data = a2b_hex(data)
        safe = self.encrypt(data)
        safe = b2a_hex(safe)
        return safe

    def parse_token(self,token):
        token = a2b_hex(token)
        try:
            token= self.decrypt(token)
            return b2a_hex(token)
        except AuthenticationError,e:
            return None


if __name__ == "__main__":
    # usage example
    data = {"channel": "unicom", "deviceType": "DoorSensor"}
    data = "bbbae7ed85e04542a6dbf2f93a89275a"
    crypt = Crypticle()
    token = crypt.get_token(data)
    print "get token:",token,len(token)
    print "parse token:",crypt.parse_token(token)
