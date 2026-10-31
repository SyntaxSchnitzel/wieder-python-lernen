gleichung1 = input("wie lautet deine erste Gleichung oder Punkt? ")  # y = k * x + d   5 = k * 5 + d
gleichung2 = input("wie lautet deine zweite Gleichung oder Punkt? ") #                 4 = k * 4 + d

def GleichungVonGleichung(gleich1,gleich2):
    gl1Splitt = gleich1.split(" ")


    gl1 = []
    for i in gl1Splitt:
        if i not in ["=","*","+"]:
            gl1.append(i)

    # gl1[0] = y wert; gl1[1] = k steigung; gl1[2] = x argument; gl1[3] = d achsenabschnitt
    funktionswert = gl1[0]
    steigung = gl1[1]
    argument = gl1[2]
    achsenabschnitt = gl1[3]


    gl2Splitt = gleich2.split(" ")

    gl2 = []
    for i in gl2Splitt:
        if i not in ["=","*","+"]:
            gl2.append(i)

    # gl2[0] = y wert; gl2[1] = k steigung; gl2[2] = x argument; gl2[3] = d achsenabschnitt
    funktionswert2 = gl2[0]
    argument2 = gl2[2]
    try:
        steigungWert = (float(funktionswert)-float(funktionswert2))/(float(argument)-float(argument2))
        achsenabschnittWert = float(funktionswert) - (float(steigungWert) * float(argument)) 


        if achsenabschnittWert >= 0:
            achsenabschnittWert1 = f"+ {achsenabschnittWert}"
        else:
            achsenabschnittWert1 = f"- {abs(achsenabschnittWert)}"

        if steigungWert == 1 and achsenabschnittWert == 0:
            funktionsGleichung = "y = x"
        elif steigungWert == 1 and achsenabschnittWert != 0:
            funktionsGleichung = f"y = x {achsenabschnittWert1}"
        elif steigungWert != 1 and achsenabschnittWert == 0:
            funktionsGleichung = f"y = {steigungWert} * x"
        else:
            funktionsGleichung = f"y = {steigungWert} * x {achsenabschnittWert1}"
        print(funktionsGleichung)

    except ZeroDivisionError:
        print("Keine Funktion: Steigung ist unendtlich")

def punkteZuFormel():   # A(1,6)
    tmp = gleichung1.split(",")
    xKoord = tmp[0][2:]
    yKoord = tmp[1][:-1]
    tmp2 = gleichung2.split(",")
    xKoord2 = tmp2[0][2:]
    yKoord2 = tmp2[1][:-1]

    GleichungVonGleichung(f"{yKoord} = k * {xKoord} + d", f"{yKoord2} = k * {xKoord2} + d")




def entscheiden():
    prüfen = list(gleichung1)
    prüfen.extend(list(gleichung2))
    for i in prüfen:
        if i in ["(",")"]:
            punkteZuFormel()
            break
    else:
        GleichungVonGleichung(gleichung1, gleichung2)

entscheiden()
