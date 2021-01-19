import sys
import os

MSGS = [ "helloworld" ]

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(x ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(x ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return os.urandom(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print(c.encode().hex())
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

main()