from utils import bi_freqs, freq_analysis, freq_weight

CTEXT = "ctext"


def rebuild_fence(ctext, rails, length):
    """Rebuilds the original fence format of the cipher.  Takes advantage of
    the triangular spacing patterns to reconstruct.

    Ex. if len(rails) == 4 then the spacing for top row will be 5 - 0 - 5...
    next 3 - 1 - 3... then 3 - 3 - 3... then 1 - 3 - 1... then 5 - 0 - 5.
    To rebuild make a spacing array [6, 4, 2, 0] and reverse the order every
    character (with some small caveats)
    """
    fence = [[None] * length for n in range(rails)]
    spacing = [2 + 2*i for i in reversed(range(rails-1))] + [0]
    ctr, offset, rail = 0, 0, 0
    for c in ctext:
        # If we've reached the end of a rail, move down to the next one
        if ctr + offset >= length:
            rail += 1
            offset += 1
            ctr = 0
            spacing.sort(reverse=True)
        fence[rail][offset + ctr] = c
        # Since we don't want to overwrite anything, if spacing is 0 reflip
        # spacing array
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
        # Rebuild fence
        fence = rebuild_fence(ctext, rails, length)

        # Derive ptext
        ptext = [None] * length
        for rail in fence:
            for i in range(len(rail)):
                if rail[i]:
                    ptext[i] = rail[i]
        ptexts.append("".join(c for c in ptext))

    # Sort ptexts by frequency analysis using bigrams
    alph = {k.upper(): v for k, v in bi_freqs.items()}
    ptexts = sorted(ptexts,
                    key=lambda x:freq_weight(freq_analysis(x, alph, 2), alph))
    for i in range(5):
        print("Possible decryption #{}:".format(i))
        print(ptexts[i]  + "\n\n")
