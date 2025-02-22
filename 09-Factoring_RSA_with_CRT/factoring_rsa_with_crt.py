# Resources: https://infoscience.epfl.ch/record/164524/files/nscan20.PDF


from math import gcd
from crypto_utils import modinv

x = 0xdeadc0de
y = 0x17d7f90a4597fb2bbbb41d1a70f505f0d8c5cb53faaafea259150eb6910fb08fbf1ba40e42de70c596fb0032d132c9c6ce46c650999ad5f14a990d205984260146e2949b819dc8732beceed452701d88b2c8723b410fce739009df89930424c566af5102403981c26c3e75d9c62065a347e815b26984dcd3b5f02fc8a8092051
n = 0x90def3c2c91ae9bf6089ec8857960d567fdbcd7c2c3ea713046977231e65f44e1b91550971d4e5d43b51675fae4ba640add3af02dad4bf68c3ddef3a98907e1e01156de7a4474d9fce2ba8c055f44673c703a72a111a06f8a7b2fe582463938d802e91630e1e1b5483b1774e608eb4368c6bbf4da375319d9a2799bf8a5ae453
e = 0x10001


if __name__ == '__main__':
    p = gcd(y**e - x, n)
    q = n // p
    tot = (p-1)*(q-1)
    d = modinv(e, tot)
    print(d % 1000000007)
