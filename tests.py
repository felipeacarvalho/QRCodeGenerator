listTeste = [0, 2, 5, 2, 3, 4, 3]

listSemDups = [x for x in listTeste if listTeste.count(x) == 1]
print(listSemDups)