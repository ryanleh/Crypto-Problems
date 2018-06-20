from utils import str_to_block

m1 = "Deposit amount: 5 dollars"
c1 = "5797791557579e322e619f12b0ccdee8802015ee0467c419e7a38bd0a254da54"
m2 = "One million dolls is quite the collection"
c2 = "b1e952572d6b8e00b626be86552376e2d529a1b9cafaeb3ba7533d2699636323e7e433c10a9dcdab2ed4bee54da684ca"
m3 = "Hey nice binoculars"
c3 = "35d0c02036354fdf6082285e0f7bd6d2fdf526bd557b045bce65a3b3e300b55e"

    
if __name__ == '__main__':
    # Correct ctext is m1[0] + m2[0] + m3[1]
    ctext_b1 = str_to_block(c1, 32)[0]
    ctext_b2 = str_to_block(c2, 32)[0]
    ctext_b3 = str_to_block(c3, 32)[1]
    ctext = ctext_b1 + ctext_b2 + ctext_b3
    print('0x' + ctext)

    # Just going to find the key for fun
    m1_0 = str_to_block(m1, 16)[0]
    c1_0 = str_to_block(c1, 32)[0]
    m1_0 = [ord(c) for c in m1_0]
    c1_0 = str_to_block(c1_0, 2)
    key = []
    for m, c in zip(m1_0, c1_0):
        key.append(format(m ^ int(c, 16), '02x'))
    print(key)
    c2_0 = str_to_block(c2, 32)[0]
    c2_0 = str_to_block(c2_0, 2)
    for c, k in zip(c2_0, key):
        print(chr(int(c, 16) ^ int(k, 16)))
    

