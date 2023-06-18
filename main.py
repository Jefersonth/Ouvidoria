def abrirBancoDados(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def encerrarBancoDados(connection):
    connection.close()

def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

def listarBancoDados(connection, sql, dados=None):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    results = cursor.fetchall()
    cursor.close()
    return results

def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas