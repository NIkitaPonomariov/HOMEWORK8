import json
import re
from mongoengine import connect
from models import Quote
import redis

connect('your_database_name', host='your_mongo_uri')

# Підключення до Redis
r = redis.Redis()

while True:
    command = input("Введіть команду: ")
    if command.startswith("name:"):
        name = command.split(":", 1)[1].strip()
        cached_quotes = r.get(name)
        if cached_quotes:
            print(json.loads(cached_quotes))
        else:
            quotes = Quote.objects(author__fullname=name)
            r.set(name, quotes.to_json())
            print(quotes)
    elif command.startswith("tag:"):
        tag = command.split(":", 1)[1].strip()
        quotes = Quote.objects(tags=tag)
        print(quotes)
    elif command.startswith("tags:"):
        tags = command.split(":", 1)[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        print(quotes)
    elif command == "exit":
        break
