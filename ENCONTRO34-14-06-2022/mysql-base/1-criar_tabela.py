import mysql.connector


cnx = mysql.connector.connect(
    user='root',
    password='123456',
    host='127.0.0.1',
    database='employees')

cursor = cnx.cursor()

TABLE_ALUNO= """CREATE TABLE aluno(
 matricula int auto_increment not null,
 nome VARCHAR(100) not null,
 primary key (matricula));"""

cursor.execute(TABLE_ALUNO)


cursor.close()
cnx.close()
