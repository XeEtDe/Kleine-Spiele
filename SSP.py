import random
def Spiel(Nochmal = False):
    if Nochmal == True:
        print("Nochmal?")
        Weiter = input()
        if Weiter == "Nein" or Weiter == "nein":
            quit()
    #Einleitung
    print("Wilkommen zu Schere Stein Papier :D")
    print("Schere - 1  Stein - 2  Papier - 3\nWähle jetzt")
    #Spieler und Computer Auswahl
    Spieler_Wahl = None
    Wahl = input()
    while Spieler_Wahl == None:
        if Wahl == "1" or Wahl == "Schere" or Wahl == "schere":
            Spieler_Wahl = "Schere"
        elif Wahl == "2" or Wahl == "Stein" or Wahl == "stein":
            Spieler_Wahl = "Stein"
        elif Wahl == "3" or Wahl == "Papier" or Wahl == "papier":
            Spieler_Wahl = "Papier"
        elif Wahl == "*" or Wahl == "Brunnen" or Wahl == "brunnen":
            Spieler_Wahl = "Brunnen"
        else:
            print("Schere - 1  Stein - 2  Papier - 3\nWähle jetzt")
            Wahl = input()
    Computer_Wahl = random.choice(["Schere", "Stein", "Papier"])
    print("Deine Wahl: " + Spieler_Wahl + " <-> " + "Computer: " + Computer_Wahl)
    #Wer gewinnt?
    #{Auswahl:Gegner Auswahl bei der Auswahl Gewinnt}
    Gewinnt_Bei = {"Schere":"Papier", "Stein":"Schere", "Papier":"Stein"}
    if Spieler_Wahl == Computer_Wahl:
        print("Unentschieden")
        Spiel(True)
    else:
        Gewinner = None
        if Spieler_Wahl == "Brunnen":
            if Computer_Wahl == "Schere" or Computer_Wahl == "Stein":
                Gewinner = True
            #else:
                #Gewinner = "Computer"
        elif Gewinnt_Bei[Spieler_Wahl] == Computer_Wahl:
            Gewinner = True
        #else:
            #Gewinner = "Computer"
        if Gewinner == True:
            print("Du gewinnst")
        else:
            print("Der Computer gewinnt")
        Spiel(True)

Spiel()
