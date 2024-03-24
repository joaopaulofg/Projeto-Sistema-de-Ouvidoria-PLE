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
    cabecalho("Inserção de Manifestação")
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
            print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
        else:
            try:
                sql = 'INSERT INTO ouvidoria(cpfManifestante, manifestante, manifestacao, telefone_1) VALUES(?, ?, ?, ?)'
                c.execute(sql, (cpfManifestante, manifestante, manifestacao, telefone_1))
            except:
                print("\nErro ao inserir manifestação.")
            else:
                print("\nManifestação inserido com sucesso!")
                con.commit()

# Listagem de manifestações existentes no sistema.
def listarManifestacoes():
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        try:
            sql = 'SELECT * FROM ouvidoria'
            c.execute(sql)
        except:
            print("Erro ao listar manifestações.")
        else:
            cabecalho("manifestações cadastradas")
            manifestacoes = c.fetchall()
            for m in manifestacoes:
                print("\nID Manifestação:", m[0], "\nCPF Manifestante:", m[1], "\nManifestante:", m[2], "\nRelato:", m[3])

# Exclusão de manifestações existentes no sistema.
def excluirManifestacao():
    cabecalho("Exclusão de Manifestação")
    idExclusao = lerInteiro("\nInsira o ID da manifestação que deseja excluir: ")
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        try:
            dsql = 'DELETE FROM ouvidoria WHERE id = ?'
            c.execute(dsql, (idExclusao,))
        except:
            print("Manifestação não encontrada.")
        else:
            print("\nA manifestação com ID ", idExclusao, " foi apagada com sucesso!")
            con.commit()

# Alteração de manifestações existentes no sistema.
def alterarManifestacao():
    cabecalho("Alteração de Manifestação")
    idAlteracao = lerInteiro("\nInsira o ID da manifestação que deseja alterar: ")
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        try:
            sql = 'SELECT * FROM ouvidoria WHERE id = ?'
            c.execute(sql, (idAlteracao,))
            alterar = c.fetchall()
        except:
            print("Erro na busca pela manifestação.")
        else:
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
                print("Erro na alteração de dados da manifestação.")
            else:
                asql = 'UPDATE ouvidoria SET cpfManifestante = ?, manifestante = ?, manifestacao = ?, telefone_1 = ? WHERE id = ?;'
                c.execute(asql, (cpfManifestante, manifestante, manifestacao, telefone_1, idAlteracao))
                con.commit()
                print("\nManifestação alterada com sucesso!")
                