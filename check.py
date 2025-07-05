import os
import datetime
import sys


if len(sys.argv) > 1:
	log_file = sys.argv[1]

else:
	data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	log_file = f"log_{data}.txt"

print("Nome do arquivo de log:", log_file)

if os.geteuid() == 0:
	print("Você é root.")

else:
    print("Você não é root.")


with open(log_file, "a") as log:
    log.write(f"Script executado por UID {os.geteuid()} em {datetime.datetime.now()}\n")

