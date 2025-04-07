import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',  
        password='',
        database='escola'
    )

def inserir_aluno(nome, idade, curso):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, idade, curso))
    conn.commit()
    conn.close()

def atualizar_aluno(id, nome, idade, curso):
    conn = conectar()  
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome=%s, idade=%s, curso=%s WHERE id=%s", (nome, idade, curso, id))
    conn.commit()
    conn.close()

def deletar_aluno(id): 
    conn = conectar()  
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id=%s", (id,))
    conn.commit()
    conn.close()

def buscar_aluno(nome):  
    conn = conectar()  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE nome=%s", (nome,))
    result = cursor.fetchall()
    conn.close()
    return result

inserir_aluno('Maycon Silva', 22, 'ADS')
atualizar_aluno(1, 'Maycon Silva', 23, 'Sistemas de Informação')
deletar_aluno(1)
print(buscar_aluno('Maycon Silva'))
