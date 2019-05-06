import time
import multiprocessing

resultat_quadratzahlen = []

def quadratzahlen(zahlen):
	print("\nBerechnung Quadratzahlen")
	global resultat_quadratzahlen
	for n in zahlen:
		print("Quadratzahl: " + str(n) + " -> " + str(n*n))
		resultat_quadratzahlen.append(n*n)
	print("Resultat im Prozess: " + str(resultat_quadratzahlen))

if __name__ == "__main__":
	liste = [2,3,4,5,6,7,8,9]
	p1 = multiprocessing.Process(target= quadratzahlen, args=(liste,))

	t = time.time()
	p1.start()
	p1.join()

print("Resultat ausserhalb: " + str(resultat_quadratzahlen))
print("\nBenötigte Zeit: ", time.time()-t)
