import random 

def bubbleSort(lista):

    e = j = aux = 0
    t = len(lista)

    for e in range(t-1):
        for j in range(t-e-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def insertionSort(lista):
    t = len(lista)
    j = e = 0

    for e in range(t):
        x =lista[e]
        j=e-1
        while j>=0 and lista[j]>x:
            lista[j+1]= lista[j]
            j-=1
        lista[j+1]=x

def selectionSort(lista):
    n = len(lista)
    i = 0
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if lista[j] > lista[min]:
                min = j
            aux = lista[j]
            lista[j] = lista[min]
            lista[min] = aux

def shellSort(lista):
    h = 1
    t = len(lista)

    while h > 0:
        for i in range(h, t):
            c = lista[i]
            j = i
            while j >= h and c < lista[j - h]:
                lista[j] = lista[j-h]
                j = j - h
                lista[j] = c
        h = int(h/2.2)
    return lista
    

def particao(Array,inicio,final): 
	i = ( inicio-1 )		
	pivo = Array[final]	

	for j in range(inicio , final): 
		if Array[j] <= pivo: 			
			i = i+1
			Array[i],Array[j] = Array[j],Array[i] 

	Array[i+1],Array[final] = Array[final],Array[i+1] 
	return ( i+1 ) 

def quickSort(Array,inicio,final): 
	if inicio < final: 
		pi = particao(Array,inicio,final) 
		quickSort(Array, inicio, pi-1) 
		quickSort(Array, pi+1, final) 

#main
lista = list()

for i in range(10):
    lista.append(random.randint(0,9))


print("Ordenação com BubbleSort: \n")
#bubbleSort(lista)

print("Ordenação com InsertionSort: \n")
#insertionSort(lista)

print("Ordenação com SeletionSort: \n")
#selectionSort(lista)

print("Ordenação com ShellSort: \n")
#shellSort(lista)

print("Ordenação com QuickSort: \n")
quickSort(lista, 0, len(lista)-1)


print(lista)




