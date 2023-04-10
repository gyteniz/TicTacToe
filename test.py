from laimejimas import Laimejimas
from lentele import Atvaizdavimas

galimi = {1,2,3,4,5,6,7,8,9}
kombinacija1 = Laimejimas()
kombinacija2 = Laimejimas()
vaizdas = Atvaizdavimas()
vaizdas.groteles(0, " ")

def ivedimas():
    while True:
        try:
            zingsnis = int(input("Iveskite lenteles pozicijos skaiciu:\t\t"))
            galimi_ejimai(zingsnis)
            return zingsnis
            break
        except ValueError:
            print("Įvedėte ne skaičių. Bandykite dar kartą")



def galimi_ejimai(zingsnis):
    # zingsnis =ivedimas()
    # galimi = {"1","2","3","4","5","6","7","8","9"}
    # galimi = {1,2,3,4,5,6,7,8,9}
    if len(galimi)<1:
        print("game over")

    elif zingsnis in galimi:
        galimi.discard(zingsnis)
        print(galimi)
        return zingsnis


    else:
        print("Sis langelis jau uzimtas")

def zymejimas(number):
    if number == 1:
        zyme = "X"

    elif number == 2:
        zyme = "O"
    return zyme

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






while True:

    print("Pirmo zaidejo ejimas")
    sk = ivedimas()
    zyme = zymejimas(1)
    vaizdas.groteles(sk, zyme)

    laimejimo_patikrinimas(1, sk)
    if kombinacija1.gauti_rezultata() == True:
        print("Laimejo pirmas zaidejas")
        break
    # if vaizdas.nuspalvinta():
    #     print("Lygiosios")

    print("Antro zaidejo ejimas")
    sk = ivedimas()
    zyme = zymejimas(2)
    vaizdas.groteles(sk, zyme)

    laimejimo_patikrinimas(2, sk)
    if kombinacija1.gauti_rezultata() == True:
        print("Laimejo antras zaidejas")
        break
    # if vaizdas.nuspalvinta():
    #     print("Lygiosios")