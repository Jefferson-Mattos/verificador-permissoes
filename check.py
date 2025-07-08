import os
import datetime
import sys
import json
import argparse
import grp
from utils.logger import enviar_log

parser = argparse.ArgumentParser(description="Verificador de permissões de usuário.")
parser.add_argument('--log', type=str, help="Nome do arquivo de log", default=f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
parser.add_argument('--json', action='store_true', help="Gerar log em JSON")
parser.add_argument('--verbose', action='store_true', help="Exibir detalhes no terminal")
args = parser.parse_args()

uid = os.geteuid()
user_is_root = uid == 0
user_in_sudo = False

try:
	user_groups = grp.getgrnam("sudo").gr_mem
	user_in_sudo = os.getlogin() in user_groups
except:
	pass

status = "root" if user_is_root else ("grupo sudo" if user_in_sudo else "usuário comum")

if args.verbose:
	print(f"Usuário: {os.getlogin()} (UID: {uid}) - permissão: {status}")

log_data = {
	"usuario": os.getlogin(),
	"uid": uid,
	"status": status,
	"data": str(datetime.datetime.now())
}

os.makedirs(os.path.dirname(args.log), exist_ok=True)

with open(args.log, "a") as log:
	if args.json:
		log.write(json.dumps(log_data) + "\n")
	else:
		log.write(f"{log_data['data']} - UID {uid} - Permissão: {status}\n")

enviar_log(log_data)

