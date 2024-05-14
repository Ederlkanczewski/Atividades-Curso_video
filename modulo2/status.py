import sqlite3
conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

sql = '''
create table status(
    id int not null,
    status varchar(100)
    primary key(id))
'''




cursor.execute(sql)
conexao.commit()
conexao.close()



