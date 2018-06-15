import math
from cryptography.hazmat.primitives import serialization as serial
from cryptography.hazmat.backends import default_backend

PUB_KEY1 = 'pub_key1.pem'
PUB_KEY2 = 'pub_key2.pem'



if __name__ == '__main__':
    pub1_pem = open('pub_key1.pem', 'br').read()
    pub2_pem = open('pub_key2.pem', 'br').read()

    pub1_rsa = serialization.load_pem_public_key(pub1_pem, default_backend())
    pub2_rsa = serialization.load_pem_public_key(pub1_pem, default_backend())

    n1 = pub1_rsa.public_numbers().n
    n2 = pub2_rsa.public_numbers().n


