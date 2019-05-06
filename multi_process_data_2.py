#Multiprocessing mit Array

import time
import multiprocessing

def quadratzahlen(zahlen, resultat_quadratzahlen):
	for idx, n in enumerate(zahlen):
		resultat_quadratzahlen[idx] = n*n
	print("\nResultat innerhalb Prozess: " + str(resultat_quadratzahlen[:]))

if __name__ == "__main__":
	liste = [2,3,4,5,6,7,8,9]
	resultat_quadratzahlen = multiprocessing.Array("i", 8) #i steht für 'integer', bei 'double' ist eine andere Syntax (Value)
	p1 = multiprocessing.Process(target= quadratzahlen, args=(liste, resultat_quadratzahlen))

	t = time.time()
	p1.start()
	p1.join()

print("\nResultat ausserhalb Prozess: " + str(resultat_quadratzahlen[:]))
print("\nBenötigte Zeit: ", time.time()-t)


#Es gäbe noch weitere möglichkeinten wie zum Beispiel die Queue