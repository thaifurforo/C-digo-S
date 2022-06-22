import mysql.connector


cnx = mysql.connector.connect(
    user='root',
    password='123456',
    host='127.0.0.1',
    database='employees')

cursor = cnx.cursor()

INSERT_ALUNO1 = "INSERT INTO aluno (nome) VALUES ('Ana Alice');"
INSERT_ALUNO2 = "INSERT INTO aluno (nome) VALUES ('Maicon Scott');"

cursor.execute(INSERT_ALUNO1)
cursor.execute(INSERT_ALUNO2)

cnx.commit()

cursor.close()
cnx.close()
