class Atvaizdavimas:
    def __init__(self):
        self.lang = [" " for x in range(9)]

    def groteles(self, sk, zyme):
        sk-=1
        self.lang[sk] = zyme
        # self.lang[1] = " "
        # self.lang[2] = " "
        # self.lang[3] = " "
        # self.lang[4] = " "
        # self.lang[5] = " "
        # self.lang[6] = " "
        # self.lang[7] = " "
        # self.lang[8] = " "
        # lang[0] = "", lang[1] = "", lang[2] = "", lang[3] = "", lang[4] = "", lang[5] = "", lang[6] = "", lang[7] = "", \
        # lang[8] = ""


        print('%s' % (9 * '.     '))

        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[6]).center(15), str(self.lang[7]).center(15), str(self.lang[8]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))

        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[3]).center(15), str(self.lang[4]).center(15), str(self.lang[5]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))

        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[0]).center(15), str(self.lang[1]).center(15), str(self.lang[2]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (9 * '.     '))

    def nuspalvinta(self):
        if " " not in self.lang:
            return True
        else:
            return False

# vaizdas=Atvaizdavimas()
# vaizdas.groteles()