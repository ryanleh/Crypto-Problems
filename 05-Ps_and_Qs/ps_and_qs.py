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
    pub2_rsa = serial.load_pem_public_key(pub2_pem, default_backend())

    n1 = pub1_rsa.public_numbers().n
    n2 = pub2_rsa.public_numbers().n

    e1 = pub1_rsa.public_numbers().e
    e2 = pub2_rsa.public_numbers().e
    gcd = (math.gcd(n1, n2))

    # Assuming gcd is prime for sake of problem

    q1 = n1 // gcd
    q2 = n2 // gcd 

    phi1 = (gcd - 1) * (q1 - 1)
    phi2 = (gcd - 1) * (q2 - 1)

    d1 = modinv(e1, phi1)
    d2 = modinv(e2, phi2)
    if d1 and d2:
        print("N1: " + str(n1))
        print("N2: " + str(n2))
        print("E1: " + str(e1))
        print("E2: " + str(e2))
        print("D1: " + str(d1))
        print("D2: " + str(d2))
    else:
        print("Modinv failed")
    


