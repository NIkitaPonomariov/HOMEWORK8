import pika
from mongoengine import connect
from models import Contact

connect('your_database_name', host='your_mongo_uri')

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts')

# Генерація контактів
contacts = [Contact(fullname="John Doe", email="john@example.com").save() for _ in range(10)]
for contact in contacts:
    channel.basic_publish(exchange='', routing_key='contacts', body=str(contact.id))

connection.close()
