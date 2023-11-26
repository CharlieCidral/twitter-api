from flask import Flask, render_template, request
from handlers.database_handler import connect_to_database, insert_user_data
from src.get_user_info import get_user_res

app = Flask(__name__)

# Defina uma rota para consumir a API
@app.route("/")
def home():
  
  return render_template("tweets.html")
  # return render_template("templates/tweets.html", user_info=user_info)

@app.route('/receive', methods=['POST'])
def receive_info():
  field = request.form.get('user_info')
  user_info = filter(field)
  return render_template("receive.html", field=field, user_info=user_info)

def filter(field):
  # Conectar ao banco de dados
  users_collection = connect_to_database()
  print(f"user collection:{users_collection}")
  # Obter dados do usuário
  user_info = get_user_res(field)
  print(f"user info:{user_info}")
  # Inserir dados do usuário no banco de dados
  insert_user_data(users_collection, user_info)
  print("inserted")
  return user_info

@app.route('/user')
def user():
  users_collection = get_all_user_documents()
  return render_template("user.html", users_collection=users_collection)


def get_all_user_documents():
  users_collection = connect_to_database()
  all_documents = list(users_collection.find())
  print(f"user collection:{users_collection}")
  return all_documents

if __name__ == "__main__":
  # Inicializa o servidor apenas se o script for executado diretamente
  app.run(debug=True)
