from laimejimas import Laimejimas

# sk1=0
# sk2=0
# sk3=0

# kombinacija1 = Laimejimas(sk1=1, sk2=1, sk3=1)

# kombinacija1.gauti_rezultata()


kombinacija1 = Laimejimas()
kombinacija2 = Laimejimas()

ivediniai = []

while True:
    # zaisti1 = input("PIRMAS ZAIDEJAS:\t\t")

    if zaisti1 not in ivediniai:
        ivediniai.append(zaisti1)
        match zaisti1:
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
    print(ivediniai)
    zaisti2 = input("ANTRAS ZAIDEJAS:\t\t")
    if zaisti2 not in ivediniai:
        ivediniai.append(zaisti2)
        match zaisti2:
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
    print(ivediniai)