from pymongo import MongoClient

client = MongoClient("mongodb+srv://180052:180052@cluster0.rslpz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.todo_app

collection_name = db["todos_app"]