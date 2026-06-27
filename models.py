from mongoengine import Document, BooleanField
from mongoengine.fields import StringField, ListField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField(max_length=120, required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {'collection': "authors"}

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'collection': "quotes"}


class Contact(Document):
    fullname = StringField(max_length=120, required=True)
    email = StringField(max_length=120, required=True)
    is_sent = BooleanField(default=False)
    meta = {'collection': "contacts"}


