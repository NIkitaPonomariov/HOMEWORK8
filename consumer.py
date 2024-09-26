import pika
from mongoengine import connect
from models import Contact

connect('your_database_name', host='your_mongo_uri')

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    # Імітація надсилання email
    print(f"Надсилаємо email для контакту: {contact.fullname}")
    contact.sent = True
    contact.save()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts')

channel.basic_consume(queue='contacts', on_message_callback=callback, auto_ack=True)
print('Очікуємо на повідомлення. Натисніть CTRL+C для виходу.')
channel.start_consuming()
