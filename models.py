from peewee import *
import datetime
import os
from playhouse.db_url import connect
from flask_login import UserMixin

connect(os.environ.get('DATABASE_URL')) 
Database=os.environ.get('DATABASE_URL')
# DATABASE = SqliteDatabase('burgers_beers.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField() 

    class Meta:
        database = os.environ.get('DATABASE_URL')

class Places(Model):
    name = CharField(50,null=True) 
    location = CharField(50) 
    rating = IntegerField(default=0)
    likes = IntegerField(default=0)
    comments = TextField()
    imageURL = CharField()
    user = ForeignKeyField(User, backref='places')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = os.environ.get('DATABASE_URL')


def initialize():
    os.environ.get('DATABASE_URL').connect()
    os.environ.get('DATABASE_URL').create_tables([User, Places], safe=True)
    print("TABLES Created")
    os.environ.get('DATABASE_URL').close()

