from banco import con

# Cabecalho
def cabecalho(msg):
    print()
    print('-'*40)
    print(msg.center(40).upper())
    print('-'*40)

# Menu Principal
def menuPrincipal():
    print('''
        [1] - Listar Manifestação
        [2] - Inserir Nova Manifestação
        [3] - Alterar Manifestação
        [4] - Excluir Manifestação
        [5] - Sair 
    ''')