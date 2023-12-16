class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # TODO

    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] + shift) % len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)

        return ''.join(ciphertext)

    def decode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = -(self.key[i % len(self.key)])
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)

        return ''.join(ciphertext)


keyword = 'мфти'
cipher = Vigenere(keyword)

line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()