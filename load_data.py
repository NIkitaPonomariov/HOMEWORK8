import json
from mongoengine import connect
from models import Author, Quote

connect('your_database_name', host='your_mongo_uri')

# Завантаження авторів
with open('authors.json') as f:
    authors_data = json.load(f)
    for author in authors_data:
        Author(**author).save()

# Завантаження цитат
with open('quotes.json') as f:
    quotes_data = json.load(f)
    for quote in quotes_data:
        author = Author.objects(fullname=quote['author']).first()
        Quote(tags=quote['tags'], author=author, quote=quote['quote']).save()
