import sqlite3, os
from lib import *

os.system('clear')

print("\n\033[1;32mBem-vindo ao meu sistema de Ouvidoria!\033[m\n")

try:
    con = sqlite3.Connection('ouvidoria.db')
    c = con.cursor()
except ConnectionError:
    print("\033[1;31mErro ao conectar ao banco de dados, favor verificar. Encerrando o sistema.\n\033[0m")
else:
    while True:
        cabecalho("menu de opções")
        menuPrincipal()
        opcao = lerInteiro("\n>>> Digite uma opcão: ")

        # Opção 1 - Listar todas as manifestações cadastradas no sistema.
        if opcao == 1:
            os.system('clear')
            listarManifestacoes()

        # Opção 2 - Listar Manifestações por tipo.
        elif opcao == 2:
            os.system('clear')
            listarManifestacoesPorTipo()

        # Opção 3 - Inserir uma nova manifestação no sistema.
        elif opcao == 3:
            os.system('clear')
            inserirManifestacao()

        # Opção 4 - Exibir quantidade de manifestações cadastradas no sistema.
        elif opcao == 4:
            os.system('clear')
            listarQuantidadeDeManifestacoes() # type: ignore

        # Opção 5 - Pesquisar manifestação por ID.
        elif opcao == 5:
            os.system('clear')
            pesquisarManifestacao()

        # Opção 6 - Excluir manifestação por ID.
        elif opcao == 6:
            os.system('clear')
            excluirManifestacao()

        # Opção 6 - Sair do sistema.
        elif opcao == 7:
            os.system('clear')
            encerrarSistema()

        # Opção inválida, caso o usuário digite um valor que não esteja no menu.
        else:
            os.system('clear')
            print("Opção inválida. Digite novamente.\n")