def abrirBancoDados(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)
