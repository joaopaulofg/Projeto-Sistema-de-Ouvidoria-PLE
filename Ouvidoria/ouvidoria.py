from lib import cabecalho, menuPrincipal, lerInteiro, inserirManifestacao, listarManifestacoes, excluirManifestacao
import os

cabecalho("ouvidoria do joão")

while True:
    cabecalho("menu de opções")
    menuPrincipal()
    op = lerInteiro("ESCOLHA UMA OPÇÃO: ")

    if op == 1:
        listarManifestacoes()
    elif op == 2:
        inserirManifestacao()
    elif op == 3:
        print()
    elif op == 4:
        excluirManifestacao()
    elif op == 5:
        print('Finalizando...')
        os.system('cls')
        print('Programa Encerrado')
        break
    else:
        print("\nOpção inválida.")