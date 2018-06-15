from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends.openssl import backend


PRIV_KEY = 'priv_key'


if __name__ == '__main__':
    priv_key = int(open(PRIV_KEY, 'r').read())
    ec_priv_key = ec.derive_private_key(priv_key,
                                        ec.EllipticCurve("secp256k1", 256),
                                        backend)
    ec_pub_key = ec_priv_key.public_key(backend)


