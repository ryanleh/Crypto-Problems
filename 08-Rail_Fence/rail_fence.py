ctext = "WECRL TEERD SOEEF EAOCA IVDEN".replace(" ", "")
rails = 3


def rebuild_fence(ctext, rails, length):
    """Rebuilds the original fence format of the cipher"""
    fence = [[None] * length for n in range(rails)]
    spacing = [(2 * rails - 2 - 2 * i) for i in range(rails // 2 + 1)] + [0]
    ctr, offset, rail = 0, 0, 0
    for c in ctext:
        if ctr + offset >= length:
            rail += 1
            offset += 1
            ctr = 0
        fence[rail][offset + ctr] = c
        if spacing[rail] == 0:
            spacing = spacing[::-1]
        ctr += spacing[rail]
        spacing = spacing[::-1]
    return fence





if __name__ == '__main__':
    length = len(ctext)
    fence = rebuild_fence(ctext, rails, length)
    ptext = [None] * length
    for rail in fence:
        for i in range(len(rail)):
            if rail[i]:
                ptext[i] = rail[i]
    print("".join(ptext))

