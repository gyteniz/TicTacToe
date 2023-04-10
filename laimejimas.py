class Laimejimas:
    def __init__(self, sk1=False, sk2=False, sk3=False, sk4=False, sk5=False, sk6=False, sk7=False, sk8=False,
                 sk9=False):
        self.sk1 = sk1
        self.sk2 = sk2
        self.sk3 = sk3
        self.sk4 = sk4
        self.sk5 = sk5
        self.sk6 = sk6
        self.sk7 = sk7
        self.sk8 = sk8
        self.sk9 = sk9


    def gauti_rezultata(self):
        # self.skaiciai = [self.sk1, self.sk2, self.sk3, self.sk4, self.sk5, self.sk6, self.sk7, self.sk8, self.sk9]
        if self.sk1 & self.sk2 & self.sk3 == True:
            self.laimejimas_print()
            return True
        elif self.sk4 & self.sk5 & self.sk6 == True:
            # print("riebalas2")
            self.laimejimas_print()
            return True
        elif self.sk7 & self.sk8 & self.sk9 == True:
            # print("riebalas3")
            self.laimejimas_print()
            return True
        elif self.sk1 & self.sk4 & self.sk7 == True:
            # print("riebalas4")
            self.laimejimas_print()
            return True
        elif self.sk2 & self.sk5 & self.sk8 == True:
            # print("riebalas5")
            self.laimejimas_print()
            return True
        elif self.sk3 & self.sk6 & self.sk9 == True:
            # print("riebalas6")
            self.laimejimas_print()
            return True
        elif self.sk1 & self.sk5 & self.sk9 == True:
            # print("riebalas7")
            self.laimejimas_print()
            return True
        elif self.sk3 & self.sk5 & self.sk7 == True:
            # print("riebalas8")
            self.laimejimas_print()
            return True
        else:
            False

    def laimejimas_print(self):
        print("LAIMEJIMAS")

