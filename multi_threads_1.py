import time

def quadratzahlen(zahlen):
	print("\nBerechnung Quadratzahlen")
	for n in zahlen:
		time.sleep(0.5)
		print("Quadratzahl: " + str(n) + " -> " + str(n*n))

def volumen(zahlen):
	print("\nBerechnung Volumen")
	for n in zahlen:
		time.sleep(0.5)
		print("Volumen: " + str(n) + " -> " + str(n*n*n))

liste = [2,3,4,5,6,7,8,9]

t = time.time()
quadratzahlen(liste)
volumen(liste)

print("\nBenötigte Zeit: ", time.time()-t)
