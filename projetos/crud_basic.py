import sqlite3

#Função para criar a tabela de usuários
def create_table():
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   balance FLOAT,
                   age INTEGER)''')
    db.commit()
    db.close()

# Adicionando usuarios
def add_user(name,age,balance):
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO users (name,age,balance) VALUES (?, ?, ?)''',(name,age,balance))
    db.commit()
    db.close()

#Listando os usuarios cadastrados
def list_users():
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()

    for user in users:
        print(user)

    db.close()
# Atualizando um usuario
def update_user_name(id,name):
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()

    cursor.execute('''UPDATE users SET name = ? WHERE id = ?''',(name,id))

    db.commit()
    db.close()

def update_user_age(id,age):
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()

    cursor.execute('''UPDATE users SET age = ? WHERE id = ?''',(age,id))

    db.commit()
    db.close()

def update_user_balance(id,balance):
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()

    cursor.execute('''UPDATE users SET balance = ? WHERE id = ?''',(balance,id))

    db.commit()
    db.close()


# Deletando um usuario
def delete_user(id):
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM users WHERE id = ?''',(id,))
    db.commit()
    db.close()

def alter_table():
    db = sqlite3.connect('crud.db')
    cursor = db.cursor()
    cursor.execute('''ALTER TABLE users ADD COLUMN balance''')
    db.commit()
    db.close()


def menu():
    print('''
    1. Adicionar usuário
    2. Listar usuários
    3. Atualizar usuário
    4. Deletar usuário
    5. Sair''')

# Criar a e atualizar a tabela com um campo novo
 
#create_table()
#alter_table()

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        name = input("Digite o nome do usuário: ")
        age = input("Digite a idade do usuário: ")
        balance = input("Digite o saldo na conta: ")

        try:
            int(age)
            add_user(name, age, balance)
            print("Usuário adicionado com sucesso!")
        except ValueError:
            print("Digite uma idade válida")

    elif escolha == '2':
        print("\nListando todos os usuários:\n")
        list_users()

    elif escolha == '3':
        print("\nLista de usuários que podem ser alterados:\n")
        list_users()

        alteracao = input('''
Selecione o que deseja alterar\n
1. Alterar a idade
2. Alterar o nome
3. Alterar o saldo\n
Digite a opcao desejada:''')
        
        if alteracao == '1':
            try:
                id = int(input("Digite o ID do usuário a ser atualizado: "))
                age = int(input("Digite a nova idade do usuário: "))
                update_user_age(id,age)
            except ValueError:
                print("Entrada inválida, tente novamente")

        elif alteracao == '2':
            try:
                id = int(input("Digite o ID do usuário a ser atualizado: "))
                name = input("Digite o novo nome do usuário: ")
                update_user_name(id,name)
                print("Usuário atualizado com sucesso!")
            except ValueError:
                print("Entrada inválida, tente novamente")

        elif alteracao == '3':
            try:
                id = int(input("Digite o ID do usuário a ser atualizado: "))
                balance = float(input("Digite o valor a ser atualizado: "))
                update_user_balance(id,balance)
            except ValueError:
                print("Entrada inválida, tente novamente")

    elif escolha == '4':
        print("\nLista de usuários que podem ser deletados:\n")
        list_users()
        try:
            id = int(input("Digite o ID do usuário a ser deletado: "))
            delete_user(id)
            print("Usuário deletado com sucesso!")
        except ValueError as error:
            print("Entrada inválida, tente novamente")

    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

