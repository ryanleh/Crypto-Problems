from subprocess import Popen, PIPE
import sys
# Wordlist: https://github.com/dwyl/english-words

CTEXT = "ctext"
WORDS = "words.txt"

def check_word(word):
    """Checks if the given word is a valid password for the ciphertext
    and returns the plaintext if so"""
    p = Popen(['gpg', '--batch', '--yes', '--passphrase', word,
                         '--decrypt', CTEXT], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if out != b'':
        return True, out
    return False, None

if __name__ == '__main__':
    # Populate wordlist
    with open(WORDS, 'r') as f:
        words = f.read().split('\n')

    # Iterate through all the words
    for i in range(len(words)):
        is_correct, decryption = check_word(words[i])
        # If word is correct break and print
        if is_correct:
            print("\n" + words[i] + " is the correct passcode for plaintext: "
                    + str(decryption, 'utf-8'))
            break
        # Show current progress through wordlist
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d %d%%" % ('='*int(i/len(words)),
            i,int(101*(i / len(words)))))
        sys.stdout.flush()
