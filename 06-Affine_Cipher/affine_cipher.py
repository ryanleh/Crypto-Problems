# Resources
# https://en.wikipedia.org/wiki/Affine_cipher

from math import gcd

ALPHABET = 'alphabet.txt'
CTEXT = 'ctext'


def affine_dec(ctext, a, b, m):
    pass

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
    elif commas == 1 and word[-1] != ',':
        return False
    return True


if __name__ == '__main__':
    alphabet = open(ALPHABET, 'r').read().strip()
    ctext = open(CTEXT, 'r').read().strip()

    # Determine modulo and populate alphabet swap dictionary
    swap_dict = {}
    m = len(alphabet)
    for i in range(m):
        swap_dict[alphabet[i]] = i

    # Determine all possible a values
    pos_a = []
    for i in range(m):
        if gcd(i, m) == 1:
            pos_a.append(i)

    # For each a, brute force all possible b values, only print
    # decryptions which use valid punctuation
    for a in pos_a:
        for b in range(m):
            ptext = affine_dec(ctext, a, b, m)
            if all([is_word(word) for word in ptext.split(' ')]):
                print("Possible decryption:")
                print(ptext + "\n\n")







