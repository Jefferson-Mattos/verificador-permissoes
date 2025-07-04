# ---- Projeto: Verificador de Permissões com log de Execução _____

# ---- Objetivo ------

# Este projeto fornece um script simples e robusto para verificar se um usuário possui privilégios de administrador (root) antes de execultar uma terefa crítica.
# Cada verificação é registrada em um arquivo de log ('registro.log') para fins de auditoria e segurança.

# ---- Tecnologias Ultilizadas -----

# - shell script (bash): usado como ponto de entrada para orquestrar a execução.
# - Python 3: Utilizado para a lógica principal de verificação de UID e escrita do log.

# ---- Como Usar -----

# ---- Pré-requisitos -----

# - Python 3 instalado
# - Um ambiente baseado em unix (Linux, macOS)

# ---- Executando -----

# 1. Dê permissão de execução para o script:

#    chmod +x check_user.sh

# 2. Depois é só rodar:

#   ./check_user.sh

# 3. E se quiser ver o histórico:

#   cat registro.log

#   Você vai ver algo como:

#   [2025-07-04 11:30:12] Script execultado por UID 1000 (sem permissão)

# --- Execução Real - versão 1 ------

# imagens tiradas durante a execução do primeiro projeto.

# --- Estrutura de arquivos -----

![estrutura arquivos](Estrura-do-arquivo.png)

# --- Conteúdo do script 'check.py' ----

![código do check.py](imagens/v1
/Conteúdo do Script.png)

# --- Execução como Usuário Normal ----

![execução usuário normal]('Usuário normal.png')

# --- Execução como root (sudo) -----

![execução root](root.png)

# --- Visualizção do log Gerado ----

![log gerado]('Visualisado o Log.png')
