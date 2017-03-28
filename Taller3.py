1. Algoritmo trivial para solucionar el problema en tiempo O(n^3)

def secuence(X):
    maximum = 0
    for i in range(0, len(X)-1):
        for j in range(i+1, len(X)):
            sum = X[j]
            for k in range(i+1, j):
                sum += X[Y]
            if sum > maximum:
                maximum = sum
    return maximum

X = [-2,11,-4,13,-5,-2]
print "la secuencia de la suma maxima es: ", secuence(X)


3 Implemente el siguiente algoritmo

def Sumamax3(a, prim, ult):
    
  #Casos base
	if prim > ult:
        	return 0
    
	if prim == ult:
        	return max(0, a[prim])
    	mitad = (prim+ult)/2
    
  #Casos 1 y 2
    	max_aux = max(Sumamax3(a, prim, mitad), Sumamax3(a, mitad+1, ult))
    
  #Casos 3: Parte izquierda
    	max_izq = 0
    	suma = 0
    	for i in range(mitad, prim-1, -1):
        	suma = suma + a[i]
        	max_izq = max(max_izq, suma)
        
  #Caso 3: Parte derecha
    	max_der = 0
    	suma = 0
    	for i in range(mitad+1, ult+1):
        	suma = suma+a[i]
        	max_der = max(max_der, suma)
    
  #Combinacion de resultados
    	return max(max_der+max_izq, max_aux)