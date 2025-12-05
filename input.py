# ==========================================
# Voorbeeld Opdracht
# Voer je naam in met de input() methode en print daarna je naam in de console.
# ==========================================

naam = input('Voer je naam in: ')  # voorbeeld invoer: Bart
print('Je naam is: ', naam)  # Het resultaat is: Je naam is: Bart


# ==========================================
# Opgave 1:
# Gegeven is het woord 'Python'. Schrijf een programma dat de gebruiker vraagt om input. Als de gebruiker het woord 'Python' invoert, print dan de boolean True, anders print False.
# ==========================================
woord = input('Voer het juiste woord in: ')

if woord == 'Python':
    print(True)
else:
    print(False)

# === HET IS LEUKER MET EEN WHILE LOOP ===
wachtwoord = input('Voer het juiste woord in: ')
while wachtwoord != 'Python':
    if wachtwoord == 'Python':
       print('Yes')
    else:
        print('Probeer opnieuw')
        wachtwoord = input('Voer het juiste woord in: ')
print('Dit was het juiste woord, tot de volgende keer!')

# ==========================================
# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt om een getal. Voer daarna nog een getal in en print de som van de twee getallen.

# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================
getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))
som = getal1 + getal2
print(f'De som van {getal1} en {getal2} is : {som}')