import pickle

Kasse = 50 #Geld zur Verfügung
Preis_Pizza = 2 #Preis der Pizza
Anzahl_Mitarbeiter = 1 #Wert wird erhöht wenn mehr eingestellt
Mitarbeiter_Produktion = 1
Lohn_Mitarbeiter = 20 #Wert kann geändert werden,pro Mitarbeiter pro Tag
Werbung = 0 #Wert wird erhöht wenn mehr Werbung gekauft
Produktion = 30 #So viele Pizzen können standartmäßig pro Tag produziert werden
Qualität = 0 #bei besserer Qualität zahlen Kunden mehr, erhöht z.B. durch Lohn und Produktionsverbesserungen (besserer Ofen, etc.)
Lieferung = 0 #für später, durch Lieferungen wird mehr verkauft
Kunden = 20 #für später
Kosten = Lohn_Mitarbeiter * Anzahl_Mitarbeiter
Zusatz_Kosten = 0
Tag_Counter = 0

#Todwerte
Negative_Kasse_Counter = 4 #Man darf drei Tage lang im minus sein bis das Spiel vorbei ist
Streik_Counter = 4 #Mitarbeiter streiken drei Tage bevor sie nacheinander kündigen

#Siegwerte
Kriterium_Pizzen = 0
Kriterium_Geld = 0
Kriterium_Mitarbeiter = 0

#Super geheimer Geheimcheat
Endless_Mode = "Aus"

Liste_Alles = [Kasse, Preis_Pizza, Anzahl_Mitarbeiter, Mitarbeiter_Produktion, Lohn_Mitarbeiter, Werbung, Produktion,
               Qualität, Lieferung, Kunden, Kosten, Zusatz_Kosten, Tag_Counter, Negative_Kasse_Counter, Streik_Counter, Kriterium_Pizzen,
               Kriterium_Geld, Kriterium_Mitarbeiter]


def Preis_Setzen(): #für Start
    global Preis_Pizza
    Preis_Pizza = float(input("Wie viel soll eine Schokipizza in deinem Laden kosten?" + "\n"))
    if Preis_Pizza < 0:
        print("O.o Das erscheint mir etwas unrealistisch. Versuchs doch nochmal.")
        Preis_Setzen()

def Start():
    print("Hallo du. Willkommen in der Schokipizzaria :D")
    print("Passe Preise, Mitarbeiter, Kapazitäten und Extrafunktionen an, um möglichst viel Umsatz zu machen und deinen Laden zu verbessern.")
    print("Dein Ziel ist es, die GOLDENE PIZZA zu gewinnen. Dafür musst du folgende Kriterien erfüllen:")
    print(" -> Eine Woche lang jeden Tag mindestens 400 Pizzen verkaufen.")
    print(" -> Eine Woche lang jeden Tag mindestens 1000 Euro Gewinn machen.")
    print(" -> Deinen Mitarbeitern mindestens 50 Euro Lohn bezahlen und mindestens 10 Mitarbeiter beschäftigen.")
    print("Dein Fortschritt wird nach jedem Tag automatisch gespeichert.")
    print("Passen wir vor deinen ersten Arbeitstag die Preise an. Die Produktionskosten einer Schokipizza betragen einen Euro.")
    Preis_Setzen()
    print("Super! Beginnen wir jetzt mit deinem ersten Tag.")
    Nächster_Tag()

#Witzige Übergangssequenz:
def Übergang(): #für Nächster_Tag
    Arbeit = 4
    Kaffee = 2
    Kunden = 4
    while Arbeit > 0:
        print("Arbeit")
        Arbeit -= 1
    while Kaffee > 0:
        print("Kaffee")
        Kaffee -= 1
    while Kunden > 0:
        print("Kunden")
        Kunden -= 1

def Nächster_Tag():
    global Anzahl_Mitarbeiter
    global Mitarbeiter_Produktion
    global Preis_Pizza
    global Fernsehn
    global Plakate
    global Produktion
    global Qualität
    global Lieferung
    global Kunden
    global Kosten
    global Zusatz_Kosten
    global Kasse
    global Negative_Kasse_Counter
    global Streik_Counter
    global Tag_Counter
    global Kriterium_Pizzen
    global Kriterium_Geld
    global Kriterium_Mitarbeiter
    global Endless_Mode
    Tag_Counter += 1
    #So viele Pizzen werden real produziert:
    Produktionsrate_ = Mitarbeiter_Produktion * Produktion
    Produktionsrate = Produktionsrate_ // 2
    #So viele Kunden kaufen eine Pizza zum gegeben Preis:
    #Startwert
    Kunden = 20
    Counter_Liste = []
    Counter_Liste.append(Tag_Counter)
    Counter = Counter_Liste.copy()
    while Counter[0] > 0:
        Kunden += 2
        Counter[0] -= 1
    #durch Werbung:
    if Plakate > 0:
        Kunden += 10
        Plakate -= 1
    if Fernsehn > 0:
        Kunden += 30
        Fernsehn -= 1
    #durch Lieferung:
    Kunden += Lieferung
    #durch Preis und Qualität:
    Preis_Liste = []
    Preis_Liste.append(Preis_Pizza)
    Preis_Counter = Preis_Liste.copy()
    Preis_Counter_1 = Preis_Liste.copy()
    Toleranz = 4 + Qualität
    while Preis_Counter[0] > Toleranz:
        Kunden -= 5
        Preis_Counter[0] -= 1
    while Preis_Counter_1[0] < Toleranz:
        Kunden += 5
        Preis_Counter_1[0] += 1
    #Grenzbereich
    if Kunden < 0:
        Kunden = 0 #Weil wär ja schon unlogisch und so
    if Kunden > 700:
        Kunden = 700 #Weil Sättigungsmenge und so
    #So viel wird verdient:
    Real_Preis = Preis_Pizza - 1
    if Produktionsrate > Kunden:
        Pizzen = Kunden
    if Kunden > Produktionsrate:
        Pizzen = Produktionsrate
    if Kunden == Produktionsrate:
        Pizzen = Kunden
    Brutto = Pizzen * Real_Preis
    Gewinn = Brutto - (Kosten + Zusatz_Kosten)
    Kasse += Gewinn
    #Witzige Übergangsequenz
    Übergang()
    print("Klo")
    Übergang()
    print("FERTIG \o/")
    print("Geld!" + "\n" + "\n")
    #Auswertung:
    print("Tag " + str(Tag_Counter))
    print("Dein heutiger Gewinn beträgt " + str(Gewinn) + " Euro, bei " + str(Pizzen) + " verkauften Schokipizzen")
    if Gewinn > 0:
        print("Gut gemacht!")
    #Hinweise
    print("\n")
    print("Hinweise:")
    #Zu Kasse und Gewinn
    if Kasse < 0:
        print("-> Du hast Schulden! Mache möglichst schnell wieder Gewinn! Sonst gehst du noch pleite :( ")
        Negative_Kasse_Counter -= 1
    if Gewinn == 0:
        print("-> Du hast heute keinen Gewinn gemacht!")
    elif Gewinn < 0:
        print("-> Du hast heute Verlust gemacht! Wenn du weiter Verluste machst, wirst du pleite gehen.")
    #Zu Mitarbeitern
    if Lohn_Mitarbeiter < 10 and Anzahl_Mitarbeiter > 0:
        if Streik_Counter > 1:
            print("-> Deine Mitarbeiter streiken wegen des niedrigen Lohnes! Bezahle ihnen wieder mehr oder sie werden nicht mehr lange hier arbeiten!")
        Streik_Counter -= 1
    #Zu Kunden und Produktion
    Kunden_ = Kunden + 5
    Produktionsrate_ = Produktionsrate + 5
    if Kunden == 0:
        print("-> Du hattest heute keine Kunden! Anscheindend ist dein Preis zu hoch.")
    elif Kunden_ < Produktionsrate:
        print("-> Du hast heute weniger Pizzen verkauft, als dein Laden produzieren kann.")
    elif Kunden > Produktionsrate_:
        print("-> Du hattest heute mehr Kunden, als du Pizzen produzieren kannst.")
    #Wenn nicht EndlessMode:
    if Endless_Mode == "An":
        #Mitarbeiter
        if Streik_Counter == 0:
            Anzahl_Mitarbeiter = 0
            Mitarbeiter_Produktion = 0
            print("\n" + "\n")
            print("Alle deine Mitarbeiter haben wegen des niedrigen Lohnes gekündigt.")
            if Lieferung > 0:
                Lieferung -= 20
                Zusatz_Kosten -= 50
                print("Der Lieferdienst wurde abgeschafft.")
            Streik_Counter = 3
        Menü()
    else:
        #Kriterien
        print("\n")
        print("Kriterien der GOLDENEN PIZZA:")
        print(" -> Eine Woche lang jeden Tag mindestens 400 Pizzen verkaufen.")
        if Pizzen > 400 or Pizzen == 400:
            Kriterium_Pizzen += 1
            if Kriterium_Pizzen == 7 or Kriterium_Pizzen > 7:
                print("Erfüllt! :D ")
            else:
                print("Noch nicht erfüllt.")
        else:
             Kriterium_Pizzen = 0
             print("Noch nicht erfüllt.")
        print(" -> Eine Woche lang jeden Tag mindestens 1000 Euro Gewinn machen.")
        if Gewinn > 1000 or Gewinn == 1000:
            Kriterium_Geld += 1
            if Kriterium_Geld == 7 or Kriterium_Geld > 7:
                print("Erfüllt! :D ")
            else:
                print("Noch nicht erfüllt.")
        else:
             Kriterium_Geld = 0
             print("Noch nicht erfüllt.")
        print(" -> Deinen Mitarbeitern mindestens 50 Euro Lohn bezahlen und mindestens 10 Mitarbeiter beschäftigen.")
        if Lohn_Mitarbeiter > 50 or Lohn_Mitarbeiter == 50 and Anzahl_Mitarbeiter > 10 or Anzahl_Mitarbeiter == 10:
            Kriterium_Mitarbeiter += 1
            print("Erfüllt! :D ")
        else:
             Kriterium_Mitarbeiter = 0
             print("Noch nicht erfüllt.")
        #Ende
        #Gewinn?
        if Kriterium_Pizzen == 7 or Kriterium_Pizzen > 7 and Kriterium_Geld == 7 or Kriterium_Geld > 7 and Kriterium_Mitarbeiter > 0:
            print("\n" + "\n")
            print("Herzlichen Glückwunsch! Du hast alle Kriterien erfüllt und die GOLDENE PIZZA gewonnen! :D ")
            Ende()
        #Verloren?
        if Negative_Kasse_Counter == 0:
            print("\n" + "\n")
            print("Du hattest jetzt zu lange Schulden und konntest diese leider nicht zurück zahlen.")
            print("Deine Pizzeria wird deshalb geschlossen. :( ")
            Ende()
        #Mitarbeiter
        if Streik_Counter == 0:
            print("\n" + "\n")
            print("Alle deine Mitarbeiter haben wegen des niedrigen Lohnes gekündigt.")
            Anzahl_Mitarbeiter = 0
            Mitarbeiter_Produktion = 0
            Lieferung -= 20
            Zusatz_Kosten -= 50
            Streik_Counter = 3
        Menü()


def Preis(): #für Menü
    global Preis_Pizza
    print("\n" + "Dein aktueller Preis beträgt " + str(Preis_Pizza) + " Euro. Die Produktionskosten einer Schokipizza betragen einen Euro.")
    Preis_Pizza = float(input("Wie hoch soll der neue Preis sein?" + "\n"))
    if Preis_Pizza < 0:
        print("O.o Das erscheint mir etwas unrealistisch. Versuchs doch nochmal.")
        Preis()
    else:
        if Preis_Pizza == 1:
          print("Der Preis wurde auf einen Euro geändert.")
        else:
            print("Der Preis wurde auf " + str(Preis_Pizza) +  " Euro geändert.")
        Menü()

def Mitarbeiter(): #für Menü
    global Anzahl_Mitarbeiter
    global Mitarbeiter_Produktion
    global Lohn_Mitarbeiter
    global Qualität
    global Kasse
    global Lieferung
    #Grammatik
    if Anzahl_Mitarbeiter == 1:
        Anzahl_ = "arbeitet ein Mitarbeiter"
    else:
        Anzahl_ = "arbeiten " + str(Anzahl_Mitarbeiter) + " Mitarbeiter"
    print("\n" + "Aktuell " + Anzahl_ + " für einen Lohn von " + str(Lohn_Mitarbeiter) + " Euro in deinem Laden.")
    print("Mehr Mitarbeiter erhöhen die Produktivität, während eine bessere Qualität durch zufriedene und gut bezahlte Mitarbeiter zu stande kommt.")
    Frage = input("Möchtest du Mitarbeiter einstellen (1) oder entlassen (2), den Lohn verändern (3) oder zurück zum Menü (4)?" + "\n")
    #Neuer Mitarbeiter
    if Frage == "1":
        Neuer_Mitarbeiter_Kosten = Anzahl_Mitarbeiter * 50
        print("Für einen neuen Mitarbeiter fallen Einarbeitungskosten von " + str(Neuer_Mitarbeiter_Kosten) + " Euro an.")
        Neuer_Mitarbeiter = input("Möchtest du einen neuen Mitarbeiter einstellen?" + "\n")
        if Neuer_Mitarbeiter == "Ja" or Neuer_Mitarbeiter == "ja":
            if Kasse < Neuer_Mitarbeiter_Kosten:
                print("Dafür scheinst du nicht genug Geld zu haben.")
                Menü()
            else:
                Kasse -= Neuer_Mitarbeiter_Kosten
                Anzahl_Mitarbeiter += 1
                Mitarbeiter_Produktion += 1
                print("Ein neuer Mitarbeiter wurde eingestellt.")
                print("Kasse: " + str(Kasse) + " Euro")
                Menü()
        else:
            Menü()
    #Mitarbeiter entlassen
    if Frage == "2":
        Entlassen = int(input("Wie viele Mitarbeiter möchtest du entlassen?" + "\n"))
        if Entlassen > (Mitarbeiter_Produktion - 1):
            print("So viele Mitarbeiter kannst du nicht enlassen, da du mindestens einen Mitarbeiter in der Produktion brauchst.")
            Mitarbeiter()
        elif Enlassen < 0:
            print("Ungültige Eingabe")
            Mitarbeiter()
        elif Enlassen == 0:
            Menü()
        else:
            Anzahl_Mitarbeiter -= Enlassen
            Mitarbeiter_Produktion -= Entlassen
            if Enlassen == 1:
                print("Ein Mitarbeiter wurde entlassen.")
            else:
                print(str(Entlassen) + " Mitarbeiter wurden entlassen")
            if Anzahl_Mitarbeiter == 1 and Lieferung > 0:
                Lieferung -= 20
                Zusatz_Kosten -= 50
                Mitarbeiter_Produktion += 1
                print("Der Lieferdienst wurde abgeschafft.")
            Menü()
    #Lohn
    elif Frage == "3":
        Lohn_Mitarbeiter = float(input("Wie viel möchtest du deinen Mitarbeitern bezahlen?" + "\n"))
        if Lohn_Mitarbeiter < 0:
            print("O.o Das erscheint mir etwas unrealistisch.")
            Mitarbeiter()
        else:
            Lohn_Liste = []
            Lohn_Liste.append(Lohn_Mitarbeiter)
            Lohn_Counter = Lohn_Liste.copy()
            while Lohn_Counter[0] > 10:
                Qualität += 1
                Lohn_Counter[0] -= 5
            print("Der Lohn beträgt nun " + str(Lohn_Mitarbeiter) + " Euro.")
            Menü()
    #Menü
    elif Frage == "4":
        Menü()
    #Ungültig
    else:
        print("Ungültige Eingabe")
        Mitarbeiter()

Maschinen = 0
Stufe = 0

def Produktionskapazitäten(): #für Menü
    global Produktion
    global Qualität
    global Maschinen
    global Stufe
    global Kasse
    #grammatikalische Korrektheit
    if Maschinen == 1:
        Anzahl_Maschinen = "eine Maschine"
    else:
        Anzahl_Maschinen = str(Maschinen) + " Maschinen"
    #Einleitung und Info
    print("\n" + "Aktuell besitzt du " + Anzahl_Maschinen + " auf Qualitätsstufe " + str(Stufe) + ", die dir bei der Arbeit helfen.")
    print("Mehr Maschinen erhöhen die Produktivität, während durch höhere Qualität mehr Kunden einen höheren Preis tolerieren.")
    Frage = input("Möchtest du mehr Maschinen kaufen (1) oder verkaufen (2), die Qualität verbessern (3) oder zurück zum Menü (4)?" + "\n")
    #Neue Maschine
    if Frage == "1":
        Maschine_Kosten = 200 * Maschinen
        if Maschine_Kosten == 0:
            Maschine_Kosten = 150
        print("Die Kosten für eine weitere Maschine betragen " + str(Maschine_Kosten) + " Euro.")
        Neue_Maschine = input("Möchtest du eine weitere Maschine kaufen?" + "\n")
        if Neue_Maschine == "Ja" or Neue_Maschine == "ja":
            if Kasse < Maschine_Kosten:
                print("Dafür scheinst du nicht genug Geld zu haben.")
                Menü()
            else:
                Kasse -= Maschine_Kosten
                Maschinen += 1
                Produktion += 10
                print("Eine neue Maschine wurde gekauft.")
                print("Kasse: " + str(Kasse) + " Euro")
                Menü()
        else:
            Menü()
    #Verkaufen
    if Frage == "2":
        print("Für jede verkaufte Maschine erhälst du 150 Euro.")
        Verkaufen = int(input("Wie viele Maschinen möchtest du verkaufen?" + "\n"))
        if Verkaufen > Maschinen:
            print("So viele Maschinen besitzt du nicht.")
            Produktionskapazitäten()
        elif Verkaufen < 0:
            print("Ungültige Eingabe")
            Produktionskapazitäten()
        elif Verkaufen == 0:
            Menü()
        else:
            Kasse += (Verkaufen * 150)
            Maschinen -= Verkaufen
            Produktion -= (10 * Verkaufen)
            if Verkaufen == 1:
                print("Eine Maschine wurde verkauft.")
            else:
                print(str(Verkaufen) + " Maschinen wurden verkauft.")
            print("Kasse: " + str(Kasse) + " Euro")
            Menü()           
    #Qualität
    elif Frage == "3":
        Kosten_Stufe = 150 * Stufe
        if Kosten_Stufe == 0:
            Kosten_Stufe = 100
        print("Die Kosten für Verbesserungen betragen " + str(Kosten_Stufe) + " Euro.")
        Nächste_Stufe = input("Möchtest du Verbesserungen kaufen?" + "\n")
        if Nächste_Stufe == "Ja" or Nächste_Stufe == "ja":
            if Kasse < Kosten_Stufe:
                print("Dafür scheinst du nicht genug Geld zu haben.")
                Menü()
            else:
                Kasse -= Kosten_Stufe
                Stufe += 1
                Qualität += 1
                print("Die Qualität wurde auf Stufe " + str(Stufe) + " verbessert.")
                print("Kasse: " + str(Kasse) + " Euro")
                Menü()
        else:
            Menü()
    #Menü
    elif Frage == "4":
        Menü()
    #Ungültig
    else:
        print("Ungültige Eingabe")
        Produktionskapazitäten()

Fernsehn = 0
Plakate = 0

def Werbung_(): #für Menü
    global Fernsehn
    global Plakate
    global Kasse
    print("\n")
    #Grammatikalische Korrektheit
    if Fernsehn == 1:
        Fernsehn_ = "einen Tag"
    else:
        Fernsehn_ = str(Fernsehn) + " Tage"
    if Plakate == 1:
        Plakate_ = "einen Tag"
    else:
        Plakate_ = str(Plakate) + " Tage"
    #Info
    if Fernsehn == 0 and Plakate == 0:
        print("Aktuell laufen keine Werbecampagnen.")
    elif Fernsehn == 0 and Plakate > 0:
        print("Werbeplakate hängen noch für " + str(Plakate_) + ", Fernseh-Werbung läuft im Moment nicht.")
    elif Fernsehn > 0 and Plakate == 0:
        print("Fernseh-Werbung läuft noch für " + str(Fernsehn_) + ", Plakate hängen im Moment nicht.")
    else:
        print("Werbeplakate hängen noch für " + str(Plakate_) + ", Fernseh-Werbung läuft noch für " + str(Fernsehn_) + ".")
    print("Werbung lässt mehr Kunden in deinen Laden kommen. Allerdings läuft sie nach einigen Tagen ab.")
    print("Fernseh-Werbung bringt dir mehr Kunden, kostet aber auch mehr als Plakate.")
    Frage = input("Möchtest du Plakate kaufen (1), Fernseh-Werbung bestellen (2) oder zurück zum Menü (3)?" + "\n")
    #Plakate
    if Frage == "1":
        Plakate_Kosten = 20
        print("Plakate kosten 20 Euro pro Tag.")
        Zeit_Plakate = int(input("Für wie viele Tage möchtest du Plakate kaufen?" + "\n"))
        if Zeit_Plakate == 0:
            Menü()
        elif Zeit_Plakate < 0:
            print("Ungültige Eingabe")
            Werbung_()
        else:
            P_Kosten = Plakate_Kosten * Zeit_Plakate
            if Kasse < P_Kosten:
                print("Dafür scheinst du nicht genug Geld zu haben.")
                Menü()
            else:
                Kasse -= P_Kosten
                Plakate += Zeit_Plakate
                if Plakate == 1:
                    print("Plakate hängen nun für einen Tag.")
                else:
                    print("Plakate hängen nun für " + str(Plakate) + " Tage.")
                print("Kasse: " + str(Kasse) + " Euro")
                Menü()
    #Fernseh
    elif Frage == "2":
        Fernseh_Kosten = 50
        print("Fernseh-Werbung kostet 50 Euro pro Tag.")
        Zeit_Fernseh = int(input("Für wie viele Tage möchtest du Fernseh-Werbung kaufen?" + "\n"))
        if Zeit_Fernseh == 0:
            Menü()
        elif Zeit_Fernseh < 0:
            print("Ungültige Eingabe")
            Werbung_()
        else:
            F_Kosten = Fernseh_Kosten * Zeit_Fernseh
            if Kasse < F_Kosten:
                print("Dafür scheinst du nicht genug Geld zu haben.")
                Menü()
            else:
                Kasse -= F_Kosten
                Fernsehn += Zeit_Fernseh
                if Fernsehn == 1:
                    print("Fernseh-Werbung läuft nun für einen Tag.")
                else:
                    print("Fernseh-Werbung läuft nun für " + str(Fernsehn) + " Tage.")
                print("Kasse: " + str(Kasse) + " Euro")
                Menü()
    #Menü
    elif Frage == "3":
        Menü()
    #Ungültig
    else:
        print("Ungültige Eingabe")
        Werbung_()
                
def Lieferdienst(): #für Menü
    global Lieferung
    global Zusatz_Kosten
    global Mitarbeiter_Produktion
    print("\n")
    if Lieferung == 0:
        if Anzahl_Mitarbeiter < 2:
            print("Für den Lieferdienst benötigst du mindestens zwei Mitarbeiter.")
            Menü()
        else:
            print("Im Moment hat deine Pizzaria keinen Lieferdienst. Durch einen Lieferdienst könntest du mehr Kunden erreichen.")
            print("Für einen Lieferdienst würde einer deiner Mitarbeiter aus der Produktion wegfallen und es würden täglich 50 Euro zusätzliche Kosten anfallen.")
            Frage = input("Möchtest du einen Lieferdienst anbieten?" + "\n")
            if Frage == "ja" or Frage == "Ja":
                Lieferung += 20
                Zusatz_Kosten += 50
                Mitarbeiter_Produktion -= 1
                print("Du hast nun einen Lieferdienst.")
                Menü()
            else:
                Menü()
    elif Lieferung > 0:
        print("Durch den Lieferdienst hast du mehr Kunden, allerdings fällt einer deiner Mitarbeiter aus der Produktion weg und es fallen täglich 50 Euro zusätzliche Kosten an.")
        Frage = input("Möchtest du den Lieferdienst abschaffen?" + "\n")
        if Frage == "ja" or Frage == "Ja":
            Lieferung -= 20
            Zusatz_Kosten -= 50
            Mitarbeiter_Produktion += 1
            print("Der Lieferdienst wurde abgeschafft.")
            Menü()
        else:
            Menü()
                
    
def Menü():
    global Kasse
    global Endless_Mode
    print("\n")
    print("Menü:")
    print("Kasse: " + str(Kasse) + " Euro")
    print("Verbessere deinen Laden oder passe Preise und Löhne an.")
    print("Tippe dafür die Nummer von einer der folgenden Möglichkeiten.")
    print("Wenn du nichts verbessern willst, tippe \"Weiter\", um den nächsten Tag zu spielen.")
    Liste_Zeug = ["Preis (1)", "Mitarbeiter (2)", "Produktionskapazitäten (3)", "Werbung (4)", "Lieferdienst (5)"]
    for x in Liste_Zeug:
        print(x)
    Input = input()
    if Input == "1":
        Preis()
    elif Input == "2":
        Mitarbeiter()
    elif Input == "3":
        Produktionskapazitäten()
    elif Input == "4":
        Werbung_()
    elif Input == "5":
        Lieferdienst()
    elif Input == "Weiter":
        Nächster_Tag()
    #Super geheimer Geheimcheat 1:
    elif Input == "Cheat":
        Kasse += 1000
        Menü()
    elif Input == "Endless":
        if Endless_Mode == "Aus":
            Endless_Mode = "An"
        elif Endless_Mode == "An":
            Endless_Mode = "Aus"
        Menü()
    else:
        print("Ungültige Eingabe")
        Menü()
        
def Ende():
    #Zurücksetzen
    global Kasse
    global Preis_Pizza
    global Anzahl_Mitarbeiter
    global Mitarbeiter_Produktion
    global Lohn_Mitarbeiter
    global Werbung
    global Produktion
    global Qualität
    global Lieferung
    global Kunden
    global Kosten
    global Zusatz_Kosten
    global Tag_Counter
    global Negative_Kasse_Counter
    global Streik_Counter
    global Kriterium_Pizzen
    global Kriterium_Geld
    global Kriterium_Mitarbeiter
    
    Kasse = 50
    Preis_Pizza = 2
    Anzahl_Mitarbeiter = 1
    Mitarbeiter_Produktion = 1
    Lohn_Mitarbeiter = 20
    Werbung = 0
    Produktion = 30
    Qualität = 0
    Lieferung = 0
    Kunden = 20
    Kosten = Lohn_Mitarbeiter * Anzahl_Mitarbeiter
    Zusatz_Kosten = 0
    Tag_Counter = 0
    Negative_Kasse_Counter = 3
    Streik_Counter = 3
    Kriterium_Pizzen = 0
    Kriterium_Geld = 0
    Kriterium_Mitarbeiter = 0

    #Weiter?
    Frage = input("Nochmal?" + "\n")
    if Frage == "Ja" or Frage == "ja":
        Start()
    else:
        quit()


Start()
