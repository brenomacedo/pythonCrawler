import itertools

string = str(input('String a ser permutada'))

resultado = itertools.permutations(string, len(string))
for i in resultado:
    print(''.join(i))
