import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))

class EngAlphabet(Alphabet):


    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.__letters_num = self.letters_num


    def letters_num(self):
        print(f'Алфавит - {self.lang}, количество букв - {int(len(self.letters)/2)}')
    #def letters_num(self): = len(letters)/2

    def is_en_letter(self, a):
        if (a in self.letters) & (self.lang == 'en'):
            print(f'{a} - это буква английского алфавита.')
        else:
            print(f'{a} - это буква НЕ английского алфавита.')
    # def letters_num(self):
    #     print(f'Алфавит - {self.lang}, количество букв - {self.letters_num}')

    @staticmethod
    def example():
        print('Пример текста на английском языке.\nHello world!')

alphaEn = EngAlphabet('en', string.ascii_letters)
alphaEn.print_letters()
alphaEn.letters_num()
alphaEn.is_en_letter('F')
alphaEn.is_en_letter('Щ')
alphaEn.example()