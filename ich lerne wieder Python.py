#gleichung1 = input("wie lautet deine erste Gleichung oder Punkt? ")  # y = k * x + d   5 = k * 5 + d
#gleichung2 = input("wie lautet deine zweite Gleichung oder Punkt? ") #                 4 = k * 4 + d

def GleichungVonGleichung(gleich, gleich2):
    gl1Splitt = gleich.split(" ")


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

        print(argument, argument2, funktionswert, funktionswert2, steigungWert, achsenabschnittWert)

        if achsenabschnittWert >= 0:
            achsenabschnittWert = f"+ {achsenabschnittWert}"
        else:
            achsenabschnittWert = f"- {abs(achsenabschnittWert)}"

        if steigungWert == 1 and achsenabschnittWert == 0:
            funktionsGleichung = "y = x"
        elif steigungWert == 1 and achsenabschnittWert != 0:
            funktionsGleichung = f"y = x {achsenabschnittWert}"
        elif steigungWert != 1 and achsenabschnittWert == 0:
            funktionsGleichung = f"y = {steigungWert} * x"
        else:
            funktionsGleichung = f"y = {steigungWert} * x {achsenabschnittWert}"
        return funktionsGleichung

    except ZeroDivisionError:
            return "Keine Funktion: Steigung ist unendtlich"

print(GleichungVonGleichung("21 = k * 5.1 + d","83 = k * 5 + d"))



