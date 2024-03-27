from lib import cabecalho, menuPrincipal, lerInteiro, inserirManifestacao, listarManifestacoes, excluirManifestacao, alterarManifestacao
import os

os.system('clear')

print("\n\033[1;32mBem-vindo ao sistema de Ouvidoria do João!\033[m")

while True:
    cabecalho("menu de opções")
    menuPrincipal()
    op = lerInteiro("ESCOLHA UMA OPÇÃO: ")

    if op == 1:
        listarManifestacoes()
    elif op == 2:
        inserirManifestacao()
    elif op == 3:
        alterarManifestacao()
    elif op == 4:
        excluirManifestacao()
    elif op == 5:
        os.system('clear')
        print("\n\033[1;32mFinalizando...\033[m")
        break
    else:
        print("\nOpção inválida.")