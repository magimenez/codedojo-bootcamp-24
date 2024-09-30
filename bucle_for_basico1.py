# basico: imprime todos los numeros enteros del 0 al 100
print("#1 enteros 0 a 100")
for i in range(100+1):
	print (i)
	
#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("#2 mutiplos 2")
for i in range(2,500+1,2):
	print(i)
	
#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
print("#3 ice ice baby")
for i in range(1,100+1):
	print(i)
	if i % 5 == 0 :
		print("ice ice")
	if i % 10 ==0:
		print("baby")
#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
print("#4 suma pares")
suma = 0
for i in range (0,500000+1, 2):
	suma = suma + i
	
print("suma = %d" % suma)
#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
print("#5 regresame al 3")
for i in range(2024, 0,-3):
	print(i)

# Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
numInicial = 3
numFinal = 10
multiplo = 2
print("#6 contador dinamico")

for i in range(numInicial, numFinal+1):
	if i % multiplo == 0: 
		print(i)
