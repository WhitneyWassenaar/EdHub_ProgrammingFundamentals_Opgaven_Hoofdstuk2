# ==========================================
# Voorbeeld Opdracht
# Schrijf de notatie van een 10 miljoen. Gebruik de ‘leesbaarheid methode’ van Python.
# print het getal.
# ==========================================

print(10_000_000)  # Het resultaat is: 10000000


# ==========================================
# Opgave 1:
# Welk getal is goed geschreven volgens de ‘leesbaarheid methode’
# print het getal.

#     100_00.000_001
#     1_000.00_001
#     1_000_000.000_1
# ==========================================
print(1_000_000.000_1)


# ==========================================
# Opgave 2:
# Hoe schrijf je de volgende getallen uit in de wetenschappelijke notatie van Python?
# print de getallen.

#     -12.000.000
#     0.13 met drie extra nullen (0.00013)
#     64.000.000.000
# ==========================================
print(-12e6)
print(0.13e-3)
print(64e9)

# ==========================================
# Opgave 3:
# Schrijf 5 miljoen uit. Hoe maak je daar met behulp van de wetenschappelijke notatie 0.05 van?
# ==========================================
# 5.000.000
print(5000000e-8)

# == JUISTE NOTATIE ===
# Ik was vergeten om de 'leesbaarheid methode' toe te passen
print(5_000_000)
print(5_000_000e-8)
# ==========================================
# Opgave 4:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.

# a. 11 * 3
# b. 7.5 – 1.5
# c. 3 + 4.0
# d. 15 / 5
# ==========================================
# a. int (Want 11 en 3 zijn hele getallen, als je die vermenigvuldigt blijven dat hele getallen)
# b. float (Want als rekent met een float zal het resultaat ook een float zijn)
# c. float (Want als rekent met een float zal het resultaat ook een float zijn)
# d. float (Want als je getallen met elkaar deelt dan zal het resultaat altijd een float zijn)


# ==========================================
# Opgave 5:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.
# a. 18 // 4
# b. 15.5 // 4
# c. 10 % 4
# d. 9 % 4.5
# ==========================================
# a. int (Want met floor division blijft het resultaat een int als je int getallen gebruikt, niet verwarren met / !)
# b. float (Want met floor division wordt het resultaat een float, het resultaat wordt naar beneden afgerond, maar blijft een float omdat 15.5 een float is)
# c. int (Want het resultaat is 2, dus een int)
# d. float (Want het 1 van de getallen is een float dus resultaat is ook een float)


# ==========================================
# Opgave 6:
# Hieronder staan een aantal expressies. Schrijf voor jezelf in een comment wat de volgorde is en reken het antwoord uit. Check dan met een print statement of je hetzelfde antwoord krijgt

#  A 8 + 2 * 3
#  B (8 + 2) * 3
#  C 2 ** 3 ** 2
#  D (2 ** 3) ** 2
#  E 100 - 5 ** 2 / 5 * 2
# ==========================================
# A 2 * 3 = 6 , 8 + 6 = 14                              | * gaat voor +
# B (8 + 2) = 10, 10 * 3 = 30                           | () gaat voor alles, daarna *
# C 3 ** 2 = 9, 2 ** 9 = 512                            | Als je alleen machtsverheffen in de berekening hebt, dan werk je van rechts naar links
# D (2 ** 3) = 8, 8 ** 2 = 64                           | () gaat voor alles, daarna machtsverheffen
# E 5 ** 2 = 25, 25 / 5 = 5, 5 * 2 = 10, 100 -10 = 90.0   | Eerst **, daarna /, daarna * en als laatste aftrekken

print(8 + 2 * 3)
print((8 + 2) * 3)
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print(100 - 5 ** 2 / 5 * 2) # In de uitwerking staat dat het resultaat 85 is, maar dat klopt niet, het hoort 90.0 te zijn

# ==========================================
# Opgave 7:
# Zet de volgende tekst om naar een Python string. Let op speciale tekens en spaties.
# Tip: Herhalende woorden kun je met een operator vaker printen
# Check het resultaat met een print statement

# A: Dit is de vorm van een dak / \
# B: ‘quotes’ ‘quotes’ ‘quotes’ ‘quotes’ spamspamspam
# C: Python’s syntax is “eenvoudig”
# ==========================================

print('Dit is de vorm van een dak / \\ ')
print(" 'quotes' " * 4, "spam" * 3) # In de uitwerking staat er 3 * 'quotes', maar ik lees toch echt 4 keer 'quotes'
print(""" Python's  syntax is "eenvoudig" """)

# === ALTERNATIEVE MANIER ===
print("Python's  syntax is \"eenvoudig\" ")

