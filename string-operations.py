# ==========================================
# Voorbeeld Opdracht
# Gegeven is de string ‘Python’ en het getal 3.
# Maak met deze variabelen de volgende string: ‘Python Python Python’ Gebruik een operator.
# ==========================================

woord = 'Python '
aantal_keer = 3

print(woord * aantal_keer)  # Het resultaat is: Python Python Python


# ==========================================
# Opgave 1:
# Maak de volgende zin in Python: Bello is 4 jaar. Dit is 28 jaar in mensenjaren.
# Je hebt de volgende variabelen: leeftijd_hond = 4 en naar_mensen_jaren = 7
# Maak een variabele aan genaamd 'mensen_jaren’. Ken daar de waarde aan toe van leeftijd_hond maal naar_mensen_jaren.
# Schrijf nu de zin met de print() methode.

# Verwachte uitkomst: Bello is 4 jaar. Dit is 28 jaar in mensenjaren.
# ==========================================
leeftijd_hond = 4
naar_mensen_jaren = 7
mensen_jaren = leeftijd_hond * naar_mensen_jaren

print(f'Bello is {leeftijd_hond} jaar. Dit is {mensen_jaren} jaar in mensenjaren.')


# ==========================================
# Opgave 2:
# Wat zijn de datatypes van de gegeven variabelen?
# Bedenk het antwoord vooraf en check het met de print() methode die het type van de variabele print.
# ==========================================

variabele_een = '5' # string (Want het getal is tussen aanhalingstekens)
variabele_twee = 1 / 1 # Float (Want bij delen is het resultaat altijd een float)
variabele_drie = 'Python' * 3 # string (Drie keer de string 'Python' blijft alsnog een string)

print(type(variabele_een))
print(type(variabele_twee))
print(type(variabele_drie))



# ==========================================
# Opgave 3:
# Niet alle variabele namen zijn toegestaan in Python. Sommige namen zijn gereserveerd voor Python zelf (keywords).
# Welke van de volgende variabele namen kun je gebruiken zonder dat je een foutmelding krijgt? Bedenk het antwoord vooraf en check het door de variabelen aan te maken.

# a.     And = ‘something’
# b.     while = ‘something’
# c.     Break = ‘something’
# d.     none = ‘something’
# ==========================================
# === WAAROM ALLEMAAL NIET? ===
# In de uitwerking staan de waarden van de variabelen tussen ‘ en ’. Dat zijn typografische aanhalingstekens en die kunnen niet in python gebruikt worden. Blijkbaar zijn deze tekens gebruikt omdat het er "mooier" uit ziet. Je gebruikt gewoon de normale aanhalingstekens zoals: " of '.
# a.     And = ‘something’    | Kan niet
# b.     while = ‘something’  | Kan niet
# c.     Break = ‘something’  | Kan niet
# d.     none = ‘something’   | Kan niet

# === JUISTE ANTWOORDEN ===
# a.     And = 'something'    | Kan wel, want in python is 'and' wel een keyword. Python is hoofdletter gevoelig dus 'And' kan weer wel
# b.     while = 'something'  | Kan niet, want while is een keyword en wordt dus gebruikt voor while loops in Python
# c.     Break = 'something'  | Kan wel, want in Python is 'break' (dus met een kleine b) wel een keyword in Python, dus met een hoofdletter kan het wel
# d.     none = 'something'   | Kan wel, want in Python is 'None' een keyword, dus none (dus met een kleine letter n) kan wel gebruikt worden

# === MAAR LIEVER GEBRUIK JE DEZE WOORDEN NIET OM VERWARRING TE VOORKOMEN :) ===
And = 'something'
# while = 'something'
Break = 'something'
none = 'something'

print(And)
print(Break)
print(none)

# ==========================================
# Opgave 4:
# Schrijf een goede variabele naam voor:

# A. Het totale aantal van een product (bananen)
# B. De minimale toegestane lengte voor een attractie in een pretpark
# C. Het grootste getal in een rij met getallen

# Denk ook aan de schrijfconventies voor variabele namen.
# ==========================================
# In python gebruik je liever snake_case
# === MIJN ANTWOORDEN ===
# A. total_bananas
# B. min_length
# C. highest_number_in_row

# === UITWERKING ===
# A. totaal_aantal_bananen
# B. min_lengte_voor_attractie
# C. grootste_getal_uit_rij

# === WAT HEB IK GELEERD? ===
# Variabelenamen mogen best langer zijn om de waarde te verduidelijken
# Een variabelenaam mag ook in het Nederlands geschreven worden :)

# ==========================================
# Opgave 5:
# Maak onderstaande opgaven
# Maak van het getal 3.14 een 3. Je mag alleen de typecast functie gebruiken
# ==========================================
getal = 3.14
getal = int(getal)

print(getal)

# === UITWERKING ==
getal = 3.14
print(int(getal))

# === WAT HEB IK GELEERD? ===
# Je mag het korter opschrijven dus gelijk in de print statement schrijven


# ==========================================
# Opgave 6:
# Gegeven zijn mijn_variabele = 5 en print(mijn_variabele * 3)
# Zorg ervoor dat de uitkomst van de print() methode ‘555’ is zonder dat je een andere getalswaarde toekent aan mijn_variabele.
# De gegeven code mag je niet aanpassen, maar je mag wel extra code toevoegen.
#
# Verwachte uitkomst: 555
# ==========================================

mijn_variabele = 5


print(str(mijn_variabele) * 3)  # Het resultaat is: 555

# === WAT HEB IK GELEERD? ===
# Van de vorige opgave heb ik geleerd dat je een variabele meteen kan typecasten dus heb ik van de variabele een string gemaakt zodat '555'geprint kan worden.


# ==========================================
# Opgave 7:
# Welke van de gegeven print() statements zullen een foutmelding veroorzaken? Bedenkt het antwoord vooraf en check het door de code uit te voeren.
# ==========================================

# Haal de # weg voor de print statements om de code te testen

# print(int('1490.99')) | Kan niet

# print(float(12))      | Kan wel

# print(int('1plus1'))  | Kan niet

# print(str(25E10))     | Kan wel

# === JUISTE ANTWOORDEN ===

# print(int('1490.99')) | Kan niet, want een int kan wel omgezet worden naar een string maar een float niet

# print(float(12))      | Kan wel, want een int kan omgezet worden naar een float

# print(int('1plus1'))  | Kan niet, want de string bevat een woord en dat kan niet omgezet worden naar een getal

# print(str(25E10))     | Kan wel, 25E10 is een wetenschappelijke notatie, namelijk: 250000000000, dus een int en een int kan wel naar een string worden omgezet
