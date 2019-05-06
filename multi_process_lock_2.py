import time
import multiprocessing

def einzahlung(kontostand, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		kontostand.value = kontostand.value + 1
		lock.release()

def abheben(kontostand, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		kontostand.value = kontostand.value - 1
		lock.release()

if __name__ == '__main__':
	kontostand = multiprocessing.Value('i', 200)

	lock = multiprocessing.Lock()

	e = multiprocessing.Process(target=einzahlung, args=(kontostand, lock))
	a = multiprocessing.Process(target=abheben, args=(kontostand, lock))

	e.start()
	a.start()

	e.join()
	a.join()

	print("\nDer Kontostand ist: " + str(kontostand.value))