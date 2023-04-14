from laimejimas import Laimejimas
from lentele import Atvaizdavimas


def ivedimas():
    while galimi:
        try:
            zingsnis = int(input("Iveskite lenteles pozicijos skaiciu:\t\t"))
            if zingsnis < 1 or zingsnis > 9:
                print("Proshalinis ivedimas")
            elif zingsnis not in galimi:
                print("Langelis uzimtas")
            else:

                galimi.discard(zingsnis)
                return zingsnis

        except ValueError:
            print("Kreivi pirstai ivede ne skaiciu")


def zymejimas(number):
    if number == 1:
        return "X"
    else:
        return "0"


def laimejimo_patikrinimas(zaidejas, skaicius):
    if zaidejas == 1:
        # ivediniai.append(skaicius)
        match skaicius:
            case 1:
                kombinacija1.sk1 = True
            case 2:
                kombinacija1.sk2 = True
            case 3:
                kombinacija1.sk3 = True
            case 4:
                kombinacija1.sk4 = True
            case 5:
                kombinacija1.sk5 = True
            case 6:
                kombinacija1.sk6 = True
            case 7:
                kombinacija1.sk7 = True
            case 8:
                kombinacija1.sk8 = True
            case 9:
                kombinacija1.sk9 = True

        kombinacija1.gauti_rezultata()
        return zaidejas

    if zaidejas == 2:
        # skaicius.append(sk)
        match skaicius:
            case 1:
                kombinacija2.sk1 = True
            case 2:
                kombinacija2.sk2 = True
            case 3:
                kombinacija2.sk3 = True
            case 4:
                kombinacija2.sk4 = True
            case 5:
                kombinacija2.sk5 = True
            case 6:
                kombinacija2.sk6 = True
            case 7:
                kombinacija2.sk7 = True
            case 8:
                kombinacija2.sk8 = True
            case 9:
                kombinacija2.sk9 = True

        kombinacija2.gauti_rezultata()
        return zaidejas


def zaisti():
    while True:
        # galimi = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        print("Pirmo zaidejo ejimas")
        sk = ivedimas()

        zyme = zymejimas(1)
        vaizdas.groteles(sk, zyme)

        laimejimo_patikrinimas(1, sk)
        if kombinacija1.gauti_rezultata() == True:
            vaizdas.pirmas_laimejo()
            break
        if vaizdas.nuspalvinta():
            vaizdas.lygiosios()
            break

        print("Antro zaidejo ejimas")
        sk = ivedimas()
        zyme = zymejimas(2)
        vaizdas.groteles(sk, zyme)

        laimejimo_patikrinimas(2, sk)
        if kombinacija2.gauti_rezultata() == True:
            vaizdas.antras_laimejo()
            break

        if vaizdas.nuspalvinta():
            vaizdas.lygiosios()
            break


kombinacija1 = Laimejimas()
kombinacija2 = Laimejimas()
vaizdas = Atvaizdavimas()
vaizdas.groteles(0, " ")
galimi = {1, 2, 3, 4, 5, 6, 7, 8, 9}
zaisti()
