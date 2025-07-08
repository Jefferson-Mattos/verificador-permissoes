# ---- Projeto: Verificador de Permissões com log de Execução - Versão 3 _____

# Versão atual: Refatorada e profissional - suporte a JSON, argparse, verificação de grupo e logs dinâmicos

# ---- Objetivo ------

# Este projeto verificar se um usuário possui privilégios de administrativos (root) antes de execultar tarefas críticas. Ele registra cada execução em um arquivo de log e , agora na versão 3, também em formato JSON, com possibilidade de personalização de nome do log e envio simulado via API (logger).

# ---- Tecnologias Ultilizadas -----

# - shell script (bash)
# - Python 3
# - Json
# - Argparse
# - Estrutura modular (util/)
# - Teste com unittest
# - Git + GitHub

# ---- Novidades da versão 3 -----

# - Argumentos via terminal com argparse 
# - Log de execução em formato JSON
# - Verificação se o usuario está no grupo sudo 
# - CLI com opções como JSON, LOG, VERBOSE
# - Esrutura de projeto modular e organizada
# - Pronto para expansão e teste automatizados

# ----- Estrutura do projeto ----

# - bash
# - verficador-permissões/
# |--check.py                         # script principal
# |--check_user.sh                    # script shell facilitador 
# |--registro.log                     # log padão em texto
# |--logs/                            # logs personalizados 
# | --- log_2025-07-05_11-30.json        
# |--imagens/                         # prints de execução
# | --- v3/  
# |--utils/                           # módulos auxiliares (ex logger.py)
# |--test/                            # testes automatizados
# | --- test/                        
# |--README.md                        # documentação
# ---- Como Usar -----

# ---- Pré-requisitos -----

# - Python 3 instalado
# - Um ambiente baseado em unix (Linux, macOS)

# ---- Executando -----

# 1. Dê permissão de execução para o script:

#    chmod +x check_user.sh

# 2. Depois é só rodar:

#   ./check_user.sh

# 3. Rodar manualmente com argumetos 

#   python3 check.py --log logs/meu_log.json --json --verbose 

# 4. Verificador logs

#   cat registro.log
#   cat logs/meu_log.json | jq 

# --- Histórico de Vesões ----

# - Versão 1: Lógica básica com log padrão

# - Checagem de root
# - Log em registro.log
# - sem argumentos

# --- Vesão 2: Argumentos via terminal + JSON ---

# - Recebe nome do log como argumento (sys.argv)
# - Suporte a log JSON com --json
# - criação dinânica de pasta(logs/)
# - prints de execução incluído
# - Estrutura modular 
# - preparado para expansão

# --- Versão 3: Testes automatizados ---

# - Verificação de grupo admin
# - Envio de log via API
# - CLI completa com argparse (--log, --json, --verbose)
# - Teste automático (pytest)
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

# --- Execução Real - versão 2 ------

# imagens tiradas durante a execução do versão 2 do projeto.

# ------ Estrutura de Arquivos -----

![estrutura arquivos](imagens/v2/estrutura_arquivos.png)

# ------ Conteúdo do Script `check.py` ----

![conteúdo do script](imagens/v2/checkpy_codigo.png)

# ------ Execução como Usuário Normal -----

![usuário normal](imagens/v2/usuario_normal.png)

# ------ Execução como root (sudo) ------

![execução root](imagens/v2/execucao_root.png)

# ------ Log Gerado -----

![log gerado](imagens/v2/log_gerado.png)

# ------ Estrutura com `tree` ------

![estrutura tree](imagens/v2/estrutura_tree.png)

# --- Execução Real - versão 3 ------

# imagens tiradas durante a execução do versão 3 do projeto.

# ------ Estrutura de Arquivos -----

![estrutura arquivos](imagens/v3/Estrutura-de-arquivo.png)

# ------ Conteúdo do Script `check.py` ----

![conteúdo do script](imagens/v3/check1.py.png)
![conteúdo do script](imagens/v3/check2.py.png)

# ------ Execução como Usuário Normal -----

![usuário normal](imagens/v3/usuario_normal_v3.png)

# ------ Execução como root (sudo) ------

![execução root](imagens/v3/root_v3.png)

# ------ Log JSON -----

![log gerado](imagens/v3/log_json_v3.png)

# ------ Estrutura com `tree` ------

![estrutura tree](imagens/v3/estrutura_tree1.png)
![estrutura tree](imagens/v3/estrutura_tree2.png)

# --- Licença ---

# MIT- Sinta-se livre para usar, modificar e contribuir! 
