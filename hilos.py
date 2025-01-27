import logging
import threading
import time


def thread_function(name):
    logging.info("Hilo %s: iniciando")
    time.sleep(2)
    logging.info("Hilo %s: finalizando")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.info("Main  :antes de crear hilo(thread)")
x = threading.Thread(target=thread_function, args=(1,))
logging.info("Main  :despues de crear hilo(thread)")
x.start()
logging.info("Main  :esperando a que el hilo termine")
x.join()
logging.info("Main  :terminado")
