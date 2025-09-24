#selition_sort.py

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

entrada = [8, 5, 6, 7, 25, 69, 23, 47, 85]
print(selection_sort(entrada))