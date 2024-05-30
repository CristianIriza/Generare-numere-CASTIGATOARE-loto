
import random

def generare_numere_6_49():
    numere = []

    while len(numere)<6:
        numar=random.randint(1,49)
        if numar not in numere:
         numere.append(numar)

    return (f"Numerele tale norocoase de astazi sunt: {numere}")

print (generare_numere_6_49())

def generare_numere_joker():
    numere = []
    joker = random.randint(1,20)
    while len(numere) < 5:
        numar = random.randint(1, 49)
        if numar not in numere:
            numere.append(numar)

    return (f"Numerele tale norocoase de astazi sunt: {numere} + jokerul {joker}")

print (generare_numere_joker())

def generare_numere_5_40():
    numere = []
    while len(numere) < 5:
        numar = random.randint(1, 40)
        if numar not in numere:
            numere.append(numar)

    return (f"Numerele tale norocoase de astazi sunt: {numere}")

print (generare_numere_5_40())
