ctext = "WECRL TEERD SOEEF EAOCA IVDEN".replace(" ", "")
rails = 3


def fence(lst, numrails):
    """Credit: https://stackoverflow.com/questions/14519227/rail-fence-cipher-looking-for-a-better-solution"""
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    return fence

if __name__ == '__main__':
    fence = fence(ctext, rails))
    ptext = [None] * len(ctext)
    for lst in fence:
	for c in lst:
	    if c:
		
