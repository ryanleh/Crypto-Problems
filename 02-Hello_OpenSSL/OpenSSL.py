from cryptography.hazmat.primitives import serialization as serial
from cryptography.hazmat.backends import default_backend

KEY = 'pri_key.pem'
CTEXT = 'ctext.txt'

if __name__ == '__main__':
    pri_key = serial.load_pem_private_key(open(KEY, 'rb').read(),
                                          None, default_backend())
    priv_nums = pri_key.private_numbers()
    pub_nums = priv_nums.public_numbers
    N = pub_nums.n
    d = priv_nums.d
    c = int(open(CTEXT, 'r').read(), 16)
    m = hex(pow(c, d, N))
    print(m)
