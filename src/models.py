import datetime
import uuid

from peewee import (
    Model,
    CharField,
    TextField,
    UUIDField,
    BooleanField,
    DateTimeField,
    SqliteDatabase,
    ForeignKeyField,
)

database = SqliteDatabase("database.db", pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    username = CharField(max_length=16, unique=True)

    class Meta:
        table_name = "users"


class Tweet(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    message = TextField()
    is_published = BooleanField(default=True)
    user = ForeignKeyField(backref="tweets", model=User)
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = "tweets"


database.create_tables([User, Tweet])
