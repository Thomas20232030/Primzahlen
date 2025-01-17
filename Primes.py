#######################################################################
#                                                                     #
#  Calculations with prime numbers                                    #
#  Thomas Hoppe November 2021                                         #
#  https://github.com/Thomas20232030/Calculations-with-prime-numbers  #
#                                                                     #
#######################################################################

import math
import time
import random
import matplotlib.pyplot as plt
from sympy import primepi


def lucaslehmer(p):
    if p == 2:
        return True
    s = 4
    m = pow(2, p) - 1
    for x in range(1, (p - 2) + 1):
        s = ((s * s) - 2) % m
    if s == 0:
        return True
    else:
        return False


def primfaktoren(n):

    f = []
    while n % 2 == 0:
        f = f + [2]
        n = n // 2
    while n % 3 == 0:
        f = f + [3]
        n = n // 3
    t = 5
    diff = 2
    w = round(math.sqrt(n))
    while t <= w:
        while n % t == 0:
            f = f + [t]
            n = n // t
        t = t + diff
        diff = 6 - diff
    if n > 1:
        f = f + [n]
    return f


def eratosthenes(end):
    is_prime = [False] * 2 + [True] * (end - 1)
    for n in range(int(end**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n*n, end+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def atkins(end):
    results = [2, 3, 5]
    sieve = [False] * (end + 1)
    factor = int(math.sqrt(end)) + 1
    for i in range(1, factor):
        for j in range(1, factor):
            n = 4 * i ** 2 + j ** 2
            if (n <= end) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * i ** 2 + j ** 2
            if (n <= end) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            if i > j:
                n = 3 * i ** 2 - j ** 2
                if (n <= end) and (n % 12 == 11):
                    sieve[n] = not sieve[n]
    for index in range(5, factor):
        if sieve[index]:
            for jndex in range(index ** 2, end, index ** 2):
                sieve[jndex] = False
    for index in range(7, end):
        if sieve[index]:
            results.append(index)
    return results


def millerrabin(n, k):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def primzahlzwillinge(end):
    all_prim = eratosthenes(end)
    twins = []
    for i in range(0, len(all_prim) - 1):
        if all_prim[i + 1] - all_prim[i] == 2:
            twins.append(all_prim[i])
            twins.append(all_prim[i + 1])
    return twins


def eingabeendwert():
    while True:
        try:
            end = int(input("Bitte den Endwert eingeben: "))
            if end <= 1:
                print("\nEndwert mindestens 2...\n")
                continue
            break
        except ValueError:
            print("\nBitte die Zahl im richtigen Format als ganze Zahl eingeben...\n")
    return end


def ausgabeauswertung(sz, sd, z, e, sw, inter):
    ez = time.time()
    d = ez - sz

    print()
    print("Berechnung gestartet am               :", sd)
    print("Berechnung beendet am                 :", time.strftime("%d.%m.%Y um %H:%M:%S"))
    print("Größe des zu untersuchenden Intervalls:", e + 1 - sw, "von", sw, "bis", e)
    if inter is True:
        print("Anzahl in diesem Intervall            :", z)
        print("Anteil in diesem Intervall            :", round((z / (e - 1) * 100), 2), "%")

    if d >= 3600:
        print("Dauer der Berechnung                  :", round(d / 3600, 2), "Stunden")

    if 3600 > d >= 60:
        print("Dauer der Berechnung                  :", round(d / 60, 2), "Minuten")

    if d < 60:
        print("Dauer der Berechnung                  :", round(d, 2), "Sekunden")

    input("\nWeiter mit jeder beliebigen Taste...")
    return


while True:

    print("\nPrimzahlenberechnungen:")
    print("-----------------------")
    print("(1) Primzahlen in einem Intervall    (2) Das Sieb des Eratosthenes")
    print("(3) Das Sieb von Atkins              (4) Die Primzahlfunktion")
    print("(5) Die Primzahlzwillinge            (6) Der Miller-Rabin-Test")
    print("(7) Die Zerlegung in Primfaktoren    (8) Die Mersenne-Primzahlen\n")
    print("(0) Ende\n")
    auswahl = input("Deine Wahl: ")

    if auswahl == "1":

        print("\nAusgabe von Primzahlen in einem definierten Intervall")
        print("-----------------------------------------------------\n")

        while True:
            try:
                anfang = int(input("Bitte den Startwert eingeben: "))
                ende = int(input("Bitte den Endwert eingeben:   "))
                if anfang < 2 or ende < anfang:
                    print("\nStartwert mindestens 2, Endwert größer als Startwert...\n")
                    continue
                break
            except ValueError:
                print("\nBitte die Zahlen im richtigen Format als ganze Zahlen eingeben...\n")

        print()
        zaehler = 0
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        for number in range(anfang, ende + 1):
            for div in range(2, number):
                if number % div == 0:
                    break
            else:
                zaehler = zaehler + 1
                print("Primzahl", zaehler, "=", number)

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, anfang, True)

    elif auswahl == "2":

        print("\nDas Sieb des Eratosthenes")
        print("-------------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        ausgabe = eratosthenes(ende)
        zaehler = (len(ausgabe))
        print("\n", ausgabe)
        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

    elif auswahl == "3":

        print("\nDas Sieb von Atkins")
        print("-------------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        ausgabe = atkins(ende)
        zaehler = (len(ausgabe))
        print("\n", ausgabe)
        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

    elif auswahl == "4":

        print("\nDie Primzahlfunktion")
        print("--------------------\n")

        zaehler = 0
        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        print()

        primlist = []
        for zaehler in range(2, ende + 1):
            primlist.append(primepi(zaehler))

        print(primlist)

        endzeit = time.time()
        dauer = endzeit - startzeit

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, False)

        plt.title("Primzahlfunktion von 2 bis " + str(ende))
        plt.scatter(list(range(2, ende + 1)), primlist)
        plt.grid(True)
        plt.axis()
        plt.ylabel("Wert der Primzahlfunktion")
        plt.xlabel("Untersuchtes Intervall")
        plt.show()

    elif auswahl == "5":

        print("\nDie Primzahlzwillinge")
        print("---------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        zwillinge = (primzahlzwillinge(ende))
        print(zwillinge)
        zaehler = int(len(primzahlzwillinge(ende)) / 2)

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

        plt.title("Primzahlzwillinge bis " + str(ende))
        plt.plot(primzahlzwillinge(ende), "o")
        plt.grid(True)
        plt.xticks([])
        plt.xlabel("Anzahl : " + str(zaehler))
        plt.show()

    elif auswahl == "6":

        print("\nDer Miller-Rabin-Test mit 40 Durchläufen")
        print("----------------------------------------\n")

        ende = eingabeendwert()
        if millerrabin(ende, 40):
            print("Dies ist eine Primzahl")
        else:
            print("Dies ist keine Primzahl")

        input("\nWeiter mit jeder beliebigen Taste...")

    elif auswahl == "7":

        print("\nPrimfaktorenzerlegung")
        print("---------------------\n")

        zahl = eingabeendwert()
        print()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        print(primfaktoren(zahl))

        endzeit = time.time()
        print("\nBerechnung gestartet am:", startdatum)
        print("Berechnung beendet am  :", time.strftime("%d.%m.%Y um %H:%M:%S"))
        dauer = endzeit-startzeit

        if dauer >= 3600:
            print("Dauer der Berechnung   :", round(dauer / 3600, 2), "Stunden")

        if 3600 > dauer >= 60:
            print("Dauer der Berechnung   :", round(dauer / 60, 2), "Minuten")

        if dauer < 60:
            print("Dauer der Berechnung   :", round(dauer, 2), "Sekunden")

        input("\nWeiter mit jeder beliebigen Taste...")

    elif auswahl == "8":

        print("\nMersenne-Primzahlen")
        print("-------------------\n")

        mp = 0
        zm = 0

        zahl = eingabeendwert()
        print()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        for mp in range(2, zahl+1):
            if lucaslehmer(mp):
                zm = zm + 1
                print(f"\nMersenne-Primzahl {zm}: 2**{mp}-1 mit der Länge {len(str(2 ** mp - 1))}\n")
                print(2 ** mp - 1)

        endzeit = time.time()
        print("\nBerechnung gestartet am:", startdatum)
        print("Berechnung beendet am  :", time.strftime("%d.%m.%Y um %H:%M:%S"))
        dauer = endzeit - startzeit

        if dauer >= 3600:
            print("Dauer der Berechnung   :", round(dauer / 3600, 2), "Stunden")

        if 3600 > dauer >= 60:
            print("Dauer der Berechnung   :", round(dauer / 60, 2), "Minuten")

        if dauer < 60:
            print("Dauer der Berechnung   :", round(dauer, 2), "Sekunden")

        input("\nWeiter mit jeder beliebigen Taste...")

    elif auswahl == "0":

        print("\nDas Programm wird beendet...")
        break

    else:

        print("\nFalsche Eingabe. Bitte wiederholen...")
