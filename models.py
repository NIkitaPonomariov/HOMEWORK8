from mongoengine import Document, StringField, ReferenceField, ListField, BooleanField

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    preferred_method = StringField(choices=["email", "sms"], default="email")
    sent = BooleanField(default=False)
