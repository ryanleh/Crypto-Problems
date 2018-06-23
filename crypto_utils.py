mono_freqs = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
                  'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
                  'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
                  'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29,
                  'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10,
                  'z': 0.07}
bi_freqs = {'en': 1.13, 'ed': 1.08, 'is': 0.86, 'ea': 1.00, 'al': 0.88,
                'an': 1.61, 'as': 0.87, 'ar': 0.98, 'at': 1.12, 'in': 2.03,
                'et': 0.76, 'es': 1.32, 'er': 1.78, 'to': 1.07, 'nd': 1.07,
                'ng': 0.89, 're': 1.41, 'th': 2.71, 'ti': 0.99, 'te': 0.98,
                'nt': 1.17, 'it': 0.88, 'ha': 0.83, 'he': 2.33, 'on': 1.32,
                'of': 0.71, 'st': 1.25, 'ou': 0.72, 'or': 1.06, 'se': 0.73}

tri_freqs = {'the': 1.81, 'ere': 0.31, 'hes': 0.24, 'and': 0.73, 'tio': 0.31,
             'ver': 0.24, 'ing': 0.72, 'ter': 0.3, 'his': 0.24, 'ent': 0.42,
             'est': 0.28, 'oft': 0.22, 'ion': 0.42, 'ers': 0.28, 'ith': 0.21,
             'her': 0.36, 'ati': 0.26, 'fth': 0.21, 'for': 0.34, 'hat': 0.26,
             'sth': 0.21, 'tha': 0.33, 'ate': 0.25, 'oth': 0.21, 'nth': 0.33,
             'all': 0.25, 'res': 0.21, 'int': 0.32, 'eth': 0.24, 'ont': 0.2}


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
    """Given a string, splits string into blocks of length size"""
    return [string[i:i+size] for i in range(0, len(string), size)]


def freq_analysis(ctext, tokens, length):
    """Returns a dictionary containing various token frequencies.  Keep in
    mind that lots of tokens outside the provided list may mess up analysis (ie.
    bigram analysis w/ spaces)"""
    freqs = {}
    total = len(ctext) // length
    for token in tokens:
        freqs[token] = 0.0
    for token in [ctext[i:i+length] for i in range(total)]:
        if token in tokens:
            freqs[token] += 1
    for token in freqs:
        freqs[token] = float(freqs[token]) / total * 100
    return freqs


def freq_weight(obs_freqs, exp_freqs):
    """Statistical weighing for observered character frequencies using
    chi-squared testing https://en.wikipedia.org/wiki/Chi-squared_test"""
    weight = 0
    for token in obs_freqs:
        if token not in exp_freqs:
            print("ERROR: Different token lists")
            return 0.0
        weight += (exp_freqs[token] - obs_freqs[token]) ** 2 / exp_freqs[token]
    return weight
