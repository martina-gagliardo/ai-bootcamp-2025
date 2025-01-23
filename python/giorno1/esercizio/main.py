print("Inizio programma")

# Assegno la variabile foo
false = 'foo'

# Questi controlli assert devono passare tutti
assert bool(True)
assert False != True
assert True is True
assert True == True
assert None != False

# Faccio alcune operazioni aritmetiche sui numeri interi
bar = 1
baz = 2
result = baz / bar

# Incremento il risultato di uno

result + 1

# Decremento il risultato di uno

result -= 1

# Controllo che il valore non sia negativo
assert result > 0

# Concateno le stringhe
message = "hello" + "world"

# Creo una lista e la estendo
li1 = [1, 2]
li1 += 3,

# Non mi ricordo come si "prepende" un valore...
#li1 =  ...

li1.insert(0,0)

#print('ecco la mia lista', li1)

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo
tu1 = (1, 2)
tu1 += (1, 3)

lista = tuple(set(tu1))

#print(lista)

assert lista == (1, 2, 3)

# Creo un dict

d1 = {}
d1["a"] = 1
d1["b"] = 2

assert d1["a"] == 1
assert d1 == {"a": 1, "b": 2}

# Cancello la chiave "b"
del d1["b"]

# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1 and "a" in d1:
    assert True
else:
    assert False


# Stampo la scritta "Ciao" tre volte poi esco
# Conto le volte che l'ho stampata
count = 0
for idx in [1, 2, 3]:
    count += 1
    print("Ciao")

# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num <= 5:
    num += 1
    print("Ciao")

print("Fine programma")

# Bonus: verifico la seguente operazione sui float
assert abs(0.1 + 0.2 - 0.3) < 0.1e9