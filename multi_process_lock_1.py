import time
import multiprocessing

def einzahlung(kontostand):
	for i in range(100):
		time.sleep(0.01)
		kontostand.value = kontostand.value + 1

def abheben(kontostand):
	for i in range(100):
		time.sleep(0.01)
		kontostand.value = kontostand.value - 1

if __name__ == '__main__':
	kontostand = multiprocessing.Value('i', 200)
	e = multiprocessing.Process(target=einzahlung, args=(kontostand,))
	a = multiprocessing.Process(target=abheben, args=(kontostand, ))

	e.start()
	a.start()

	e.join()
	a.join()

	print("\nDer Kontostand ist: " + str(kontostand.value))