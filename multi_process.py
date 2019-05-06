import time
import multiprocessing

def quadratzahlen(zahlen):
	print("\nBerechnung Quadratzahlen")
	for n in zahlen:
		time.sleep(0.5)
		print("\nQuadratzahl: " + str(n) + " -> " + str(n*n))

def volumen(zahlen):
	print("\nBerechnung Volumen")
	for n in zahlen:
		time.sleep(0.5)
		print("\nVolumen: " + str(n) + " -> " + str(n*n*n))

if __name__ == "__main__":
	liste = [2,3,4,5,6,7,8,9]
	p1 = multiprocessing.Process(target= quadratzahlen, args=(liste,))
	p2 = multiprocessing.Process(target= volumen, args=(liste,))

	t = time.time()
	p1.start()
	p2.start()

	p1.join()
	p2.join()

print("\nBenötigte Zeit: ", time.time()-t)