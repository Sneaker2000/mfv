from argparse import ArgumentParser

class encrypt:
    def __init__(self, text):
        self.text = text
        self.output = ''
        self.i = 0
        self.alphabet_dict = {}
        for i in range(26):
            letter = chr(ord('A') + i)
            self.alphabet_dict[letter] = i + 1

    def encrypt(self, key):
        for t in self.text:
            if t != ' ':
                self.i += 1
                zahl = self.alphabet_dict[t]
                self.output += str(key * zahl * self.i)
                self.output += ' '
        return self.output

class decrypt:
    def __init__(self, cipher):
        self.output = ''
        self.i = 0
        self.alphabet_dict = {}
        for i in range(26):
            self.letter = chr(ord('A') + i)
            self.alphabet_dict[i + 1] = self.letter
        
        self.cipher = cipher.split(' ')

    def decrypt(self, key):
        for t in self.cipher:
            if t != ' ':
                self.i += 1
                self.zahl = int(t) / self.i / key
                self.output += (self.alphabet_dict[self.zahl])
        return self.output

def main():
    parser = ArgumentParser(description="Encrypt and decrypt text with a key")
    parser.add_argument("-e", "--encrypt", help="Encrypt text", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Decrypt text", action="store_true")
    parser.add_argument("-t", "--text", help="Text to encrypt or decrypt", required=True)
    parser.add_argument("-k", "--key", help="Key to encrypt or decrypt", required=True)
    args = parser.parse_args()

    text = args.text
    key = args.key

    if args.encrypt:
        e = encrypt(text.upper())
        print(e.encrypt(int(key)))
    elif args.decrypt:
        d = decrypt(text)
        print(d.decrypt(int(key)))
    else:
        print("Please specify if you want to encrypt or decrypt")

if __name__ == "__main__":
    main()