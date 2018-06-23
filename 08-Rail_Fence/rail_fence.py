from math import ceil
from utils import std_english_freqs, freq_analysis, freq_weight

CTEXT = "ctext"


def rebuild_fence(ctext, rails, length):
    """Rebuilds the original fence format of the cipher"""
    fence = [[None] * length for n in range(rails)]
    spacing = [2 + 2*i for i in reversed(range(rails-1))] + [0]
    ctr, offset, rail = 0, 0, 0
    for c in ctext:
        if ctr + offset >= length:
            rail += 1
            offset += 1
            ctr = 0
            spacing.sort(reverse=True)
        fence[rail][offset + ctr] = c
        if spacing[rail] == 0:
            spacing = spacing[::-1]
        ctr += spacing[rail]
        spacing = spacing[::-1]
    return fence


if __name__ == '__main__':
    ctext = open(CTEXT, 'r').read().replace(' ', '').strip()
    length = len(ctext)
    ptexts = []
    for rails in range(2, 20):
        # Rebuild fence, derive ptext, order by freq analysis
        fence = rebuild_fence(ctext, rails, length)
        ptext = [None] * length
        for rail in fence:
            for i in range(len(rail)):
                if rail[i]:
                    ptext[i] = rail[i]
        ptexts.append("".join(c for c in ptext))

    alph = {k.upper(): v for k, v in std_english_freqs.items()}
    #ptexts = sorted(ptexts,
    #                key=lambda x:freq_weight(freq_analysis(x, alph), alph))
    for i in range(15):
        print("Possible decryption #{}:".format(i))
        print(ptexts[i]  + "\n\n")'''

