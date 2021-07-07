class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):

        return len(self.letters)

alph_1 = Alphabet('english', 'abcdefghigklmnopqrstuw')
a = alph_1.letters
print(alph_1.lang)
print(alph_1.letters)
print(alph_1.print())
print(alph_1.letters_num())

