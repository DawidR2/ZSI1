import random


def wczytajPlik(plik):
    with open(plik, "r") as file:
        listy = list(map(str.split, file.read().splitlines()[1:]))

        symetria = []

        for i in range(len(listy)):
            symetria.append([x[i] for x in listy[i + 1:]])

        macierz = [i + j for i, j in zip(listy, symetria)]

        return macierz


def wyswieltMacierz(macierz):
    for row in macierz:
        print(row)


def losujTrasy(macierz, n):
    # print("Osobniki")
    trasy = []

    for i in range(n):
        lista = macierz[0]
        trasa = []
        while True:
            element = random.randint(0, (len(lista) - 1))
            if element not in trasa:
                trasa.append(element)

            elif len(trasa) == len(lista):
                break

        if trasa not in trasy:
            trasy.append(trasa)
        else:
            continue

    # for row in trasy:
    # print(row)

    return trasy


def ocena(macierz, trasa):
    lista = macierz[0]
    ocena = 0
    for x in range(len(lista) - 1):
        odleglosc = macierz[trasa[x]][trasa[x + 1]]
        ocena += int(odleglosc)
    temp = macierz[trasa[-1]][trasa[0]]
    ocena = ocena + int(temp)

    return ocena


def turniejowa(osobniki, n, k):
    # print('Turniejowa')
    najlepsze = []
    for i in range(n):
        losy = []
        wynik = []
        oceny = []

        while len(losy) != k:
            x = random.randint(0, (len(osobniki) - 1))
            if x not in losy:
                losy.append(x)

        for item in losy:
            wynik.append(osobniki[item])

        for item in wynik:
            oceny.append(ocena(macierz, item))
        min_value = min(oceny)
        min_index = oceny.index(min_value)
        najlepsze.append(wynik[min_index])

    # for item in najlepsze:
    # print(item, '=', ocena(macierz, item))
    return najlepsze


def krzyzowanie(selekcja, p):
    # print('Krzyżowanie')
    for i in range(len(selekcja)-1):
            los = random.uniform(0, 1)
            if los < p:
                trasa1 = selekcja[i]
                trasa2 = selekcja[i + 1]

                cut1 = random.randint(1, (len(trasa1) - 2))
                cut2 = random.randint(cut1 + 1, (len(trasa1) - 1))

                wycinek1 = trasa1[cut1:cut2]
                wycinek2 = trasa2[cut1:cut2]

                nowa_trasa1, nowa_trasa2 = [], []

                # tworzenie krzyżowania trasy 1
                for i in range(len(trasa1)):
                    if i not in range(cut1, cut2):
                        if trasa2[i] not in wycinek1:
                            nowa_trasa1.append(trasa2[i])
                        else:
                            temp = wycinek1.index(trasa2[i])
                            for j in range(len(wycinek1)):
                                dodaj = wycinek2[temp]
                                if dodaj not in wycinek1:
                                    nowa_trasa1.append(dodaj)
                                    break
                                else:
                                    temp = wycinek1.index(dodaj)
                    else:
                        nowa_trasa1.append(trasa1[i])

                # tworzenie krzyżowania trasy 2
                for i in range(len(trasa2)):
                    if i not in range(cut1, cut2):
                        if trasa1[i] not in wycinek2:
                            nowa_trasa2.append(trasa1[i])
                        else:
                            temp = wycinek2.index(trasa1[i])
                            for j in range(len(wycinek2)):
                                dodaj = wycinek1[temp]
                                if dodaj not in wycinek2:
                                    nowa_trasa2.append(dodaj)
                                    break
                                else:
                                    temp = wycinek2.index(dodaj)
                    else:
                        nowa_trasa2.append(trasa2[i])
                # print(nowa_trasa1, nowa_trasa2,'po krzyżowaniu')

                selekcja[selekcja.index(trasa1)] = nowa_trasa1
                selekcja[selekcja.index(trasa2)] = nowa_trasa2

    return selekcja



def mutacja(populacja, p):
    for i in range(len(populacja)):
        los = random.uniform(0, 1)
        if los < p:

            cut1 = random.randint(1, len(populacja[i]) - 2)
            cut2 = random.randint(cut1 + 1, len(populacja[i]) - 1)
            temp = populacja[i][cut1:cut2]
            temp.reverse()

            populacja[i][cut1:cut2] = temp

        else:
            pass

    return populacja


def wyswietl(populacja):
    oceny = []
    for item in populacja:
        oceny.append(ocena(macierz, item))

        #print(*item, ocena(macierz, item), sep='-')
    min_value = min(oceny)
    min_index = oceny.index(min_value)
    best = populacja[min_index]
    print('najlepsza trasa:')
    print(*best, sep='-', end=' ')
    print(min_value)


def algorytm(n):
    populacja = trasy
    for i in range(n):
        selekcja = turniejowa(populacja, 200, 13)
        populacja = krzyzowanie(selekcja, 0.5)
        populacja = mutacja(populacja, 0.5)
    return populacja


macierz = wczytajPlik('berlin52.txt')
# wyswieltMacierz(macierz)
trasy = losujTrasy(macierz, 200)
nowa_populacja = algorytm(10000)
wyswietl(nowa_populacja)
