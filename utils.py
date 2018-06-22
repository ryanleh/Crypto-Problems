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

def freq_analysis(alphabet, ctext):
    """Returns a dictionary containing various letter frequencies.  Doesn't
    consider any characters not in the alphabet"""
    freqs = {}
    total = len(ctext)
    for char in alphabet:
        freqs[char] = 0
    for char in ctext:
        if char not in alphabet:
            total -= 1
            pass
        else:
            freqs[char] += 1
    if total == 0:
        print("ERROR: Ciphertext didn't contain any letters from the alphabet")
    else:
        if total < len(ctext):
            print("WARNING: Some letters were excluded from analysis")
        for char in freqs:
            freqs[char] = float(freqs[char]) / total * 100
        return freqs

