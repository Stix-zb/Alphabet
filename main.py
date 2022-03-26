import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def letters_num(self):
        print(f'Алфавит - {self.lang}, количество букв - {len(self.letters)}')

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__()
        self.__letters_num = self.letters_num()

    def is_en_letter(self, a):
        if (a in self.letters) & (self.lang == 'en'):
            print('Это буква английского алфавита.')
        else:
            print('Это буква НЕ английского алфавита.')
    def letters_num(self):
        print(f'Алфавит - {self.lang}, количество букв - {len(self.__letters_num)}')

    @staticmethod
    def example():
        print('Пример текста на английском языке.\nHello world!')

alphaEn = EngAlphabet('en', string.ascii_letters)
alphaEn.print_letters()
alphaEn.letters_num()