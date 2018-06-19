# Resources
# https://en.wikipedia.org/wiki/Affine_cipher

from math import gcd
from utils import modinv

ALPHABET = 'alphabet.txt'
CTEXT = 'ctext'


def affine_dec(ctext_num, a, b, m):
    a_inv = modinv(a, m)
    ptext = [(a_inv*(num - b) % m) for num in ctext_num]
    return ptext

def is_word(word):
    """Simple word checking by asserting that a word doesn't have multiple
    commas or periods in it"""
    periods = word.count('.')
    commas = word.count(',')
    if periods > 1:
        return False
    elif periods == 1 and word[-1] != '.':
        return False
    elif commas > 1:
        return False
    return True


if __name__ == '__main__':
    alphabet = open(ALPHABET, 'r').read().strip()
    ctext = open(CTEXT, 'r').read().strip()

    # Determine modulo and populate swap dictionaries
    m = len(alphabet)
    alpha_to_num = {}
    num_to_alpha = {}
    for i in range(m):
        alpha_to_num[alphabet[i]] = i
        num_to_alpha[i] = alphabet[i]


    # Determine all possible a values
    pos_a = []
    for i in range(m):
        if gcd(i, m) == 1:
            pos_a.append(i)

    # Convert ciphertext to numbers
    ctext_num = [alpha_to_num[c] for c in ctext]

    # For each a, brute force all possible b values, only print
    # decryptions which use valid punctuation
    for a in pos_a:
        for b in range(m):
            ptext_num = affine_dec(ctext_num, a, b, m)
            ptext = "".join([num_to_alpha[num] for num in ptext_num])
            if all([is_word(word) for word in ptext.split(' ')]):
                print("Possible decryption ({}, {}): ".format(a, b))
                print(ptext + "\n\n")
            






