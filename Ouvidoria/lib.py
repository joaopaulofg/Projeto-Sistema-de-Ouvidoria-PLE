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

# Leitura de entradas no formato número inteiro.
def lerInteiro(txt):
    while True:
        try:
            entrada = int(input(txt))
        except:
            print("Digite um valor inteiro")
        else:
            break
    return entrada

# Leitura de entradas no formato texto.
def leiaTexto(txt):
    while True:
        try:
            ent = str(input(txt))
        except:
            if ent.isnumeric():
                print("Formato inválido, tente novamente.")
            else:
                break
        return ent

# Inserção de manifestações no sistema.
def inserirManifestacao():
    try:
        while True:
            cpfManifestante = leiaTexto("Insira seu CPF: ").strip()
            break
        while True:
            manifestante = leiaTexto("Insira seu nome: ").strip()
            break
        while True:
            manifestacao = leiaTexto("Insira o seu relato da manifestação: ").strip()
            break
        while True:
            telefone_1 = leiaTexto("Insira seu telefone para contato: ").strip()
            break
    except:
        print("Erro na inserçao de dados da manifestação.")
    else:
        try:
            c = con.cursor()
        except:
            print("Erro ao conectar no banco de dados;")
        else:
            try:
                sql = ('INSERT INTO ouvidoria(cpfManifestante, manifestante, manifestacao, telefone_1) SELECT "'+cpfManifestante+'", "'+manifestante+'", "'+manifestacao+'", "'+telefone_1+'"')
                c.execute(sql)
            except:
                print("Erro ao inserir manifestação.")
            else:
                print("Manifestação inserido com sucesso!")
                con.commit()