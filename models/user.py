import json
from datetime import datetime

from mongoengine import *


class User(Document):
    email = StringField(unique=True, required=True, max_length=50)
    firstname = StringField(required=True, max_length=30)
    lastname = StringField(required=True, max_length=30)
    telephone = StringField(required=True, max_length=12)
    password = StringField(required=True, max_length=200)

    def json(self):
        user_dict = {
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "telephone": self.telephone,
            "password": self.password
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["email", "firstname", "lastname"]
    }


class Device(DynamicDocument):
    iot_id = StringField(unique=True, required=True)
    user = ReferenceField(User)
    date_connected = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["iot_id"]
    }
