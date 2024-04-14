import sqlite3

try:
    con = sqlite3.Connection('ouvidoria.db')
    c = con.cursor()
except ConnectionError:
    print('\033[1;31mErro ao tentar conectar-se ao banco\033[m')
else:
    try:
        sql = ''' CREATE TABLE IF NOT EXISTS ouvidoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpfManifestante VARCHAR(11),
            manifestante VARCHAR(50),
            tipoManifestacao VARCHAR(15),
            manifestacao VARCHAR(200),
            telefone_1 VARCHAR(14));
            '''
        c.execute(sql)
    except:
        print('Erro ao criar tabela')
    else:
        print('ok')