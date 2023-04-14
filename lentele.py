class Atvaizdavimas:
    def __init__(self):
        self.lang = [" " for x in range(9)]

    def groteles(self, sk, zyme):

        sk = sk - 1
        self.lang[sk] = zyme

        print('%s' % (9 * '.     '))

        print('7%s|8%s|9%s' % ((15 * " "), (14 * " "), (15 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[6]).center(15), str(self.lang[7]).center(15), str(self.lang[8]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))

        print('4%s|5%s|6%s' % ((15 * " "), (14 * " "), (15 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[3]).center(15), str(self.lang[4]).center(15), str(self.lang[5]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (49 * '_'))

        print('1%s|2%s|3%s' % ((15 * " "), (14 * " "), (15 * " ")))
        print('.%s|%s|%s.' % (str(self.lang[0]).center(15), str(self.lang[1]).center(15), str(self.lang[2]).center(15)))
        print('%s|%s|%s' % ((16 * " "), (15 * " "), (16 * " ")))
        print('%s' % (9 * '.     '))

    def nuspalvinta(self):
        if " " not in self.lang:
            return True
        else:
            return False

    def lygiosios(self):
        print("    _                 _           _           ")
        print("   | |               (_)         (_)          ")
        print("   | |    _   _  __ _ _  ___  ___ _  ___  ___ ")
        print("   | |   | | | |/ _` | |/ _ \/ __| |/ _ \/ __|")
        print("   | |___| |_| | (_| | | (_) \__ \ | (_) \__ \ ")
        print("   |______\__, |\__, |_|\___/|___/_|\___/|___/")
        print("           __/ | __/ |                        ")
        print("          |___/ |___/                         ")

    def pirmas_laimejo(self):
        print(' _____ _                            _       _             _  _       _ _ _  ')
        print('|  __ (_)                          | |     (_)           (_)(_)     | | | | ')
        print('| |__) | _ __ _ __ ___   __ _ ___  | | __ _ _ _ __ ___   ___ _  ___ | | | | ')
        print("|  ___/ | '__| '_ ` _ \ / _` / __| | |/ _` | | '_ ` _ \ / _ \ |/ _ \| | | | ")
        print('| |   | | |  | | | | | | (_| \__ \ | | (_| | | | | | | |  __/ | (_) |_|_|_| ')
        print('|_|   |_|_|  |_| |_| |_|\__,_|___/ |_|\__,_|_|_| |_| |_|\___| |\___/(_|_|_) ')
        print('                                                           _/ |             ')
        print('                                                          |__/              ')

    def antras_laimejo(self):
        print("                _                   _       _             _  _       _ _ _  ")
        print("    /\         | |                 | |     (_)           (_)(_)     | | | | ")
        print("   /  \   _ __ | |_ _ __ __ _ ___  | | __ _ _ _ __ ___   ___ _  ___ | | | | ")
        print("  / /\ \ | '_ \| __| '__/ _` / __| | |/ _` | | '_ ` _ \ / _ \ |/ _ \| | | | ")
        print(" / ____ \| | | | |_| | | (_| \__ \ | | (_| | | | | | | |  __/ | (_) |_|_|_| ")
        print("/_/    \_\_| |_|\__|_|  \__,_|___/ |_|\__,_|_|_| |_| |_|\___| |\___/(_|_|_) ")
        print("                                                           _/ |             ")
        print("                                                          |__/              ")
