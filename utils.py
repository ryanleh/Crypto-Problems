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

def str_to_block(string, size):
        return [string[i:i+size] for i in range(0, len(string), size)]

