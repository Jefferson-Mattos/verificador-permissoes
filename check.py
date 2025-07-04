import os
import datetime

if os.geteuid() == 0:
	print("Você é root.")
else:
    print("Você não é root.")
with open("registro.log", "a") as log:
    log.write(f"Script executado por UID {os.geteuid()} em {datetime.datetime.now()}\n")

