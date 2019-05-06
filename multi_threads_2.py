import time
import threading

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

t1 = threading.Thread(target=quadratzahlen, args=(liste,))
t2 = threading.Thread(target=volumen, args=(liste,))

t1.start()
t2.start()

t1.join()
t2.join()

print("\nBenötigte Zeit: ", time.time()-t)
