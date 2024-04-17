from banco import con
import os

# Cabecalho
def cabecalho(msg):
    print('-'*40)
    print(msg.center(40).upper())
    print('-'*40)
    print()

# Menu Principal
def menuPrincipal():
    print("1 - Listar todas as manifestações\n"
    "2 - Listar manifestações por tipo\n"
    "3 - Inserir manifestação\n"
    "4 - Exibir quantidade de manifestações\n"
    "5 - Pesquisar manifestação por ID\n"
    "6 - Excluir manifestação por ID\n"
    "7 - Sair")

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
def lerTexto(txt):
    while True:
        try:
            ent = str(input(txt))
        except:
            if ent.isnumeric():
                print("Formato inválido, tente novamente.")
            else:
                break
        return ent

def switch_case(value):
    return {
        '1': 'Elogio',
        '2': 'Reclamação',
        '3': 'Sugestão',
    }.get(value, 'Valor inválido')

# Listagem de todas as manifestações existentes no sistema.
def listarManifestacoes():
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        sql = 'SELECT * FROM ouvidoria'
        c.execute(sql)
        listaDeManifestacoes = c.fetchall()

        if len(listaDeManifestacoes) == 0:
            print("Nenhuma manifestação cadastrada.")
        else:
            print("--- MANIFESTAÇÕES CADASTRADAS ---")

            for manifestacao in listaDeManifestacoes:
                print("\033[33m\nManifestação - ID #", str(manifestacao[0]).rstrip(), "\033[0m", sep='')
                print("CPF manifestante:", manifestacao[1])
                print("Manifestante:", manifestacao[2])
                print("Tipo da manifestação:", manifestacao[3])
                print("Descrição:", manifestacao[4])

            print("\n-------- FIM DA LISTAGEM --------")
    
    input("\nPressione qualquer tecla para continuar...")
    os.system('clear')

# Listagem de manifestações por tipo.
def listarManifestacoesPorTipo():
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        sql = 'SELECT * FROM ouvidoria'
        c.execute(sql)
        listaDeManifestacoes = c.fetchall()

        if len(listaDeManifestacoes) == 0:
            print("Não há manifestações cadastradas.")
        else:
            while True:
                print("Qual o tipo da manifestação que você deseja inserir:\n"
                            "\n1 - Elogio\n"
                            "2 - Reclamação\n"
                            "3 - Sugestão\n")
                    
                tipo = lerTexto(">>> Digite uma opcão: ")

                if tipo in ['1', '2', '3']:
                    tipoManifestacao = switch_case(tipo)
                    break
                else:
                    print("Opção inválida. Digite novamente.")

            sql = 'SELECT * FROM ouvidoria WHERE tipoManifestacao = ?'
            c.execute(sql, (tipoManifestacao,))
            listaDeManifestacoes = c.fetchall()

            if len(listaDeManifestacoes) == 0:
                print("Não há manifestações cadastradas com esse tipo.")
            else:
                os.system('clear')
                print("--- MANIFESTAÇÕES DO TIPO " + tipoManifestacao.upper() + " CADASTRADAS ---")
            
                for manifestacao in listaDeManifestacoes:
                    print("\033[33m\nManifestação - ID #", str(manifestacao[0]).rstrip(), "\033[0m", sep='')
                    print("CPF manifestante:", manifestacao[1])
                    print("Manifestante:", manifestacao[2])
                    print("Tipo da manifestação:", manifestacao[3])
                    print("Descrição:", manifestacao[4])
                print("\n---------------- FIM DA LISTAGEM ----------------")

        input("\nPressione qualquer tecla para continuar...")
        os.system('clear')

# Inserção de manifestações no sistema.
def inserirManifestacao():
    os.system('clear')
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        try:
            print("-------- INSERÇÃO DE MANIFESTAÇÃO --------")
            while True:
                cpfManifestante = lerTexto("\nInsira seu CPF: ").strip()
                break

            while True:
                manifestante = lerTexto("Insira seu nome: ").strip()
                break

            while True:
                print("Qual o tipo da manifestação que você deseja inserir:\n"
                        "\n1 - Elogio\n"
                        "2 - Reclamação\n"
                        "3 - Sugestão\n")
                
                tipo = lerTexto(">>> Digite uma opcão: ")

                if tipo in ['1', '2', '3']:
                    tipoManifestacao = switch_case(tipo)
                    break
                else:
                    print("Opção inválida. Digite novamente.")

            while True:
                manifestacao = lerTexto("Insira o seu relato da manifestação: ").strip()
                break

            while True:
                telefone_1 = lerTexto("Insira seu telefone para contato: ").strip()
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
                    sql = 'INSERT INTO ouvidoria(cpfManifestante, manifestante, tipoManifestacao, manifestacao, telefone_1) VALUES(?, ?, ?, ?, ?)'
                    c.execute(sql, (cpfManifestante, manifestante, tipoManifestacao, manifestacao, telefone_1))
                    id = c.lastrowid
                except:
                    print("\nErro ao inserir manifestação.")
                else:
                    con.commit()
                    print("\nManifestação cadastrada com sucesso! ID: " + str(id))
                    input("\nPressione qualquer tecla para continuar...")
                    os.system('clear')

# Listagem da quantidade de manifestações cadastradas no sistema.
def listarQuantidadeDeManifestacoes():
    print("Em desenvolvimento...")
    input("\nPressione qualquer tecla para continuar...")

# Pesquisa de manifestações por ID.
def pesquisarManifestacao():
    os.system('clear')
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        print("--- PESQUISA DE MANIFESTAÇÃO POR ID ---")
        idPesquisa = lerTexto("\nInsira o ID da manifestação que deseja pesquisar: ")
        sql = 'SELECT * FROM ouvidoria WHERE id = ?'
        c.execute(sql, (idPesquisa,))
        manifestacao = c.fetchall()

        if manifestacao == []:
            print("\nNão localizamos nenhuma manifestação cadastrada com esse ID.")
        else:
            for campo in manifestacao:
                print("\033[33m\nManifestação - ID #", str(campo[0]).rstrip(), "\033[0m", sep='')
                print("CPF manifestante:", campo[1])
                print("Manifestante:", campo[2])
                print("Tipo da manifestação:", campo[3])
                print("Descrição:", campo[4])

        input("\nPressione qualquer tecla para continuar...")
        os.system('clear')

# Exclusão de manifestações existentes no sistema.
def excluirManifestacao():
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        print("--- EXCLUSÃO DE MANIFESTAÇÃO ---")
        exclusao = lerTexto("\nInsira o ID da manifestação que deseja excluir: ")
        sql = 'SELECT * FROM ouvidoria WHERE id = ?'
        c.execute(sql, (exclusao,))
        manifestacao = c.fetchall()

        if manifestacao == []:
                print("\nNão localizamos nenhuma manifestação cadastrada com esse ID.")
                resultado = ""
        else:
            for campo in manifestacao:
                print("\033[33m\nManifestação - ID #", str(campo[0]).rstrip(), "\033[0m", sep='')
                print("Tipo da Manifestação:", campo[1])
                print("Manifestante:", campo[2])
                print("Descrição:", campo[3])

            while True:
                confirmacao = input("\nConfirma a exclusão da manifestação abaixo? S/N:").upper()
                if confirmacao == 'S':
                    try:
                        sql = 'DELETE FROM ouvidoria WHERE id = ?'
                        c.execute(sql, (exclusao,))
                    except:
                        print("\nErro ao excluir manifestação.")
                    else:
                        con.commit()
                        resultado = "\nManifestação excluída com sucesso!\n"
                        break
                elif confirmacao == 'N':
                    resultado = "\nExclusão cancelada.\n"
                    break
                else:
                    print("\nOpção inválida. Digite novamente.")
        
        print(resultado)
        input("Pressione qualquer tecla para continuar...")
        os.system('clear')

# Alteração de manifestações existentes no sistema.
def alterarManifestacao():
    try:
        c = con.cursor()
    except:
        print('\033[1;31mErro ao tentar conectar-se ao banco de dados.\033[m')
    else:
        print("--- ALTERAÇÃO DE MANIFESTAÇÃO ---")
        idAlteracao = lerTexto("\nInsira o ID da manifestação que deseja alterar: ")
        sql = 'SELECT * FROM ouvidoria WHERE id = ?'
        c.execute(sql, (idAlteracao,))
        manifestacao = c.fetchall()

        if manifestacao == []:
                print("\nNão localizamos nenhuma manifestação cadastrada com esse ID.")
                resultado = ""
        else:
            for campo in manifestacao:
                print("\033[33m\nManifestação - ID #", str(campo[0]).rstrip(), "\033[0m", sep='')
                print("Tipo da Manifestação:", campo[1])
                print("Manifestante:", campo[2])
                print("Descrição:", campo[3])

            while True:
                confirmacao = input("\nDeseja alterar essa manifestação? S/N:").upper()

                if confirmacao == 'S':
                    while True:
                        manifestacao = lerTexto("Insira o novo relato da manifestação: ").strip()
                        break

                    try:
                        asql = 'UPDATE ouvidoria SET manifestacao = ? WHERE id = ?;'
                        c.execute(asql, (manifestacao, idAlteracao))
                    except:
                        print("\nErro ao alterar manifestação.")
                    else:
                        con.commit()
                        resultado = "\nManifestação alterada com sucesso!\n"
                        break
                elif confirmacao == 'N':
                    resultado = "\Alteração cancelada.\n"
                    break
                else:
                    print("\nOpção inválida. Digite novamente.")
        
        print(resultado)
        input("Pressione qualquer tecla para continuar...")
        os.system('clear')

def encerrarSistema():
    os.system('clear')
    print("\n\033[1;32mFinalizando...\033[m")
    con.close()
    exit()