from math import ceil

CTEXT = "ctext"


def rebuild_fence(ctext, rails, length):
    """Rebuilds the original fence format of the cipher"""
    print(rails)
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
    for rails in range(2, 20):
        fence = rebuild_fence(ctext, rails, length)
        ptext = [None] * length
        for rail in fence:
            for i in range(len(rail)):
                if rail[i]:
                    ptext[i] = rail[i]
        print("".join(ptext))
