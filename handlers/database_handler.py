from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
user_info = None
uri = os.getenv("MONGO_URI") # Obter o URI do MongoDB a partir de variáveis de ambiente
print("MONGO_URI:", os.getenv("MONGO_URI"))

tweet_colect = os.getenv("tweet_colect") # Obter o nome do banco de dados MongoDB de variáveis de ambiente
print("tweet_colect:", os.getenv("tweet_colect"))

def connect_to_database():
    # Crie um novo cliente e conecte-se ao servidor
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[tweet_colect]
    try:
        # Tenta encontrar um documento na coleção 'users'
        users_collection = db.users
        users_collection.find_one()
        print(f"you are connected at the database. \nDocs: {users_collection}")
    except Exception as e:
        print("Falha na conexão:", e)
    return users_collection


def insert_user_data(users_collection, user_info):
    users_collection.insert_one(user_info)