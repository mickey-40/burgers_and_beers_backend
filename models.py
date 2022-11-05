from peewee import *
import datetime
from flask_login import UserMixin


DATABASE = SqliteDatabase('burgers_beers.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField() 

    class Meta:
        database = DATABASE

class Places(Model):
    name = CharField() 
    location = CharField() 
    rating = IntegerField
    likes = IntegerField
    comments = CharField()
    imageURL = CharField()
    private = BooleanField()
    user = ForeignKeyField(User, backref='places')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Places], safe=True)
    print("TABLES Created")
    DATABASE.close()

