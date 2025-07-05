# ---- Projeto: Verificador de Permissões com log de Execução - Versão 2 _____

# Versão atual: Refatorada para ser mais proficional, reutilizável e flexível

# ---- Objetivo ------

# Este projeto fornece um script robusto para verificar se um usuário possui privilégios de administrativos (root) e registra cada execução em um log. A nova versão permite especificar dinamicamente o nome do arquivo de log, tornando o script mais reutilizável e adaptável.

# ---- Tecnologias Ultilizadas -----

# - shell script (bash): usado como ponto de entrada para orquestrar a execução.
# - Python 3: Utilizado para a lógica principal de verificação de UID e escrita do log.
# - Log Dinâmico: Nome do log pode ser passado por argumento

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

#   você pode mudar o nome do arquivo de log editando o check_use.sh ou passando manualmente:

#   python3 check.py "meu_log_personalizado.log"

#   Você vai ver algo como:

#   [2025-07-04 11:30:12] Script execultado por UID 1000 (sem permissão)

# --- Execução Real - versão 1 ------

# imagens tiradas durante a execução do primeiro projeto.

# --- Estrutura de arquivos -----

![estrutura arquivos](imagens/v1/estrutura_arquivos.png)

# --- Conteúdo do script 'check.py' ----

![conteudo do script](imagens/v1/checkpy_codigo.png)

# --- Execução como Usuário Normal ----

![execucao usuario normal](imagens/v1/usuario_normal.png)

# --- Execução como root (sudo) -----

![execucao root](imagens/v1/execucao_root.png)

# --- Visualização do log Gerado ----

![log gerado](imagens/v1/log_gerado.png)

# --- Estrutura com o comando tree ----

![estrutura tree](imagens/v1/estrutura_tree.png)

# --- Licença ---

# MIT- Sinta-se livre para usar, modificar e contribuir! 
