CTEXT = 'ctext.txt'

def decaesar(shift, ctext):
    ptext = ''
    for char in ctext:
        ptext += chr(ord('A') + (ord(char) - ord('A') - shift) % 26)
    return ptext

if __name__ == '__main__':
    ctext = open('ctext.txt', 'r').read()
    for shift in range(1, 26):
        print("Key: " + chr(ord('A') + shift))
        print(decaesar(shift, ctext))
        print('')
