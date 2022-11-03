from peewee import *
import datetime

DATABASE = SqliteDatabase('burgers_beers.sqlite')


class Places(Model):
    name = CharField()
    location = CharField()
    rating = int
    likes = int
    comments = CharField()
    imageURL = CharField()
    private = BooleanField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Places], safe=True)
    print("TABLES Created")
    DATABASE.close()

