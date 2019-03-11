from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    title = CharField()
    date = CharField()
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE


def initialize():
    """ Create Entry table in case that it is not 
        already exist """
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()