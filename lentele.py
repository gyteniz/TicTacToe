class Atvaizdavimas:
    def __init__(self, lang1=1, lang2=2, lang3=3, lang4=4, lang5=5, lang6=6, lang7=7, lang8=8, lang9=9):
        self.lang1 = lang1
        self.lang2 = lang2
        self.lang3 = lang3
        self.lang4 = lang4
        self.lang5 = lang5
        self.lang6 = lang6
        self.lang7 = lang7
        self.lang8 = lang8
        self.lang9 = lang9

    def groteles(self):
        lang1 = 1
        lang2 = 2
        lang3 = 3
        lang4 = 4
        lang5 = 5
        lang6 = 6
        lang7 = 7
        lang8 = 8
        lang9 = 9

        print('%s' % (9 * '.     '))
        print('.%s|%s|%s.' % (str(lang1).rjust(15), str(lang2).rjust(15), str(lang3).rjust(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))
        print('.%s|%s|%s.' % (str(lang4).rjust(15), str(lang5).rjust(15), str(lang6).rjust(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))
        print('.%s|%s|%s.' % (str(lang7).rjust(15), str(lang8).rjust(15), str(lang9).rjust(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (9 * '.     '))
