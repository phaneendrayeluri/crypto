import sys
import os

MSGS = [ "The secret message is: When using a stream cipher, never use the key more than once" ]

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
    # key = random(1024)
    key = b'f9n\xc2\x89\xc3\x89\xc3\x9b\xc3\x98\xc3\x8c\xc2\x98t5*\xc3\x8dc\xc2\x95\x10.\xc2\xaf\xc3\x8ex\xc2\xaa\x7f\xc3\xad(\xc2\xa0\x7fk\xc3\x89\xc2\x8d)\xc3\x85\x0bi\xc2\xb03\xc2\x9a\x19\xc3\xb8\xc2\xaa@\x1a\xc2\x9cmp\xc2\x8f\xc2\x80\xc3\x80f\xc3\x87c\xc3\xbe\xc3\xb0\x121H\xc3\x8d\xc3\x98\xc3\xa8\x02\xc3\x90[\xc2\xa9\xc2\x87w3]\xc2\xae\xc3\xbc\xc3\xac\xc3\x95\xc2\x9cC:k&\xc2\x8b`\xc2\xbfN\xc3\xb0<\xc2\x9aa'
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

main()