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


std_english_freqs = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
                     'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
                     'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
                     'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29,
                     'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10,
                     'z': 0.07}


def freq_analysis(ctext, alphabet=std_english_freqs.keys()):
    """Returns a dictionary containing various letter frequencies.  Doesn't
    consider any characters not in the alphabet"""
    freqs = {}
    total = len(ctext)
    for char in alphabet:
        freqs[char] = 0
    for char in ctext:
        if char not in alphabet:
            total -= 1
        else:
            freqs[char] += 1
    if total == 0:
        print("ERROR: Ciphertext didn't contain any letters from the alphabet")
    else:
        if total < len(ctext):
            print("WARNING: Some letters were excluded from analysis")
        for char in freqs:
            freqs[char] = float(freqs[char]) / total * 100
        return freqs.orderl


def freq_weight(obs_freqs, exp_freqs=std_english_freqs):
    """Statistical weighing for observered character frequencies using
    chi-squared testing https://en.wikipedia.org/wiki/Chi-squared_test"""
    weight = 0
    for char in obs_freqs:
        weight += (exp_freqs[char] - obs_freqs[char]) ** 2 / exp_freqs[char]
    return weight
