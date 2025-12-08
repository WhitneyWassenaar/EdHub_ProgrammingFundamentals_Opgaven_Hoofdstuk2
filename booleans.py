# ==========================================
# Voorbeeld Opdracht
# Gebruik de not operator om het tegenovergestelde van de boolean waarde True te printen.
# ==========================================

print(not True)     # Het resultaat is: False


# ==========================================
# Opgave 1.
# Gebruik logische operatoren om te controleren of het getal 5 zowel groter is dan 3 als kleiner dan 10.
# Print het resultaat.
# Controleer daarna of 5 groter is dan 10 of gelijk is aan 5.
#
# Verwachte uitkomst is de boolean waarde: True
# ==========================================
print(10 > 5 > 3)
print(10 < 5 or 5 == 5)


# ==========================================
# Opgave 2.
# Evalueer of het getal 7 zowel groter is dan 5 als kleiner dan 12, en tegelijkertijd niet gelijk is aan 10.
# Print het resultaat.
#
# Verwachte uitkomst: True
# ==========================================
print(12 > 7 > 5 and 7 != 10)


# ==========================================
# Opgave 3
# Gegeven is x = 5 en y = -5
# Gebruik logische operatoren om te controleren of de variabelen positief zijn en kleiner dan 10. Print het resultaat als boolean waarde.
#
# Verwachte uitkomst voor x is: True
# Verwachte uitkomst voor y is: False
# ==========================================

x = 5
y = -5

print(10 > x > 0)
print(10 > y > 0)


print(x > 0 and x < 10)
print(y > 0 and y < 10)




# ==========================================
# Opgave 5.
# Geef aan wat het resultaat zou zijn van de volgende code:

# A. print(True or 1 / 0)
# B. print(True or False)
# C. print(False and True and True)
# D. print(True or False or False)
# E. print(not True or False or not True)
# ==========================================

# === MIJN ANTWOORDEN ===
# True (Want als 1 van de twee True is dan kijkt Python niet meer verder naar de andere mogelijkheden)
# True (Want hetzelfde als de eerste)
# False (De uitkomst kan nooit True zijn als er ook False aanwezig is. Voor 'and' kan het True zijn als beide zijden True zijn)
# True (Zodra er in een 'or' evaluatie een True waarde voorkomt, is het resultaat True)
# False (Want not True == False, dan heb je False en daarna weer not True == False, dus allemaal False)


# ==========================================
# Opgave 6:
# Evalueer of een nummer even of oneven is.
# Maak een variabele 'nummer' aan met de waarde 42,
# Schrijf de evaluatie die bepaalt of het nummer even of oneven is. Print de string 'Even' als het nummer even is, anders print 'Oneven'.
# Tip: Als het nummer gedeeld door 2 geen restwaarde heeft, dan is het even. Anders is het oneven.
# ==========================================
nummer = 42

if nummer % 2 == 0:
    print('Even')
else:
    print('Oneven')


# ==========================================
# Opgave 7:
# Begroeting op Basis van het Uur van de Dag
#
# Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
# Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen"; als het minder dan 18 is, zeg "Goedemiddag"; en anders, zeg "Goedenavond".
# Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.
#
# Check het resultaat met de print() methode. Veranderde de waarde van 'uur' om te zien of de begroeting verandert.
# ==========================================
# === KLADBLOK ===
# Ochtend 06:00 - 12:00
# Middag 12:00 - 18:00
# Avond 18:00 - 22:00

uur = 9

if uur >= 6 and uur < 12:
    print('Goedemorgen!')
elif uur >= 12 and uur < 18:
    print('Goedemiddag!')
else:
    print('Goedenavond!')

# === verkorte versie ===

uur = 12

if 12 > uur >= 6:
    print('Goedemorgen!')
elif 18 > uur >= 12:
    print('Goedemiddag!')
else:
    print('Goedenavond!')

# =========================================

# === Variabele aanroepen ===

uur = 21
begroeting = 'Goedemorgen!' if 12 > uur >= 6 else 'Goedemiddag' if  18 > uur >= 12 else 'Goedenavond!'
print(begroeting)

# Opgave 8:
# Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren. Print daarna de som en het product van de getallen.
# De input functie moet vragen 'Voer eerste getal in:' en 'Voer tweede getal in:'
# Zorg ervoor dat de input ook kommagetallen accepteert.
#
# Verwachte uitkomst bij invoer van getallen 2 en 3: De som van 2 en 3 is : 5
# ==========================================
getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))

print('De som van',getal1,'en',getal2,'is : ',(getal1 + getal2) )

# === Variabele aanroepen ===
som = getal1 + getal2
print('De som van',getal1,'en',getal2,'is : ',som )

# === Gebruik van f-string ===
print(f'De som van {getal1} en {getal2} is :  {som}')

print(True or 1 / 0)