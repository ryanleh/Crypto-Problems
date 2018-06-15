import math
import sys
from cryptography.hazmat.primitives import serialization as serial
from cryptography.hazmat.backends import default_backend

PUB_KEY1 = 'pub_key1.pem'
PUB_KEY2 = 'pub_key2.pem'


def modinv(e, phi):
    """Uses the extended Euclidean Algorithm to calculate
    the multiplicative inverse of e modulo phi. 
    Credit: https://crypto.stackexchange.com/questions/5889/calculating-rsa-
    private-exponent-when-given-public-exponent-and-the-modulus-fact"""
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None


if __name__ == '__main__':
    pub1_pem = open('pub_key1.pem', 'br').read()
    pub2_pem = open('pub_key2.pem', 'br').read()

    pub1_rsa = serial.load_pem_public_key(pub1_pem, default_backend())
    pub2_rsa = serial.load_pem_public_key(pub1_pem, default_backend())

    n1 = pub1_rsa.public_numbers().n
    n2 = pub2_rsa.public_numbers().n
    e1 = pub1_rsa.public_numbers().e
    gcd = math.gcd(n1, n2)

    for i in range(2, int(gcd/2+1)):
        if (gcd % i == 0):
            print("GCD is not a prime")
            sys.exit(1)
    print("GCD is a prime, p1=p2=gcd. Continuing")

    q1 = n1 / gcd
    phi = (gcd - 1)(q1 - 1)
    d1 = modinv(e1, phi)
    print("D is: " + d1)
    
    


