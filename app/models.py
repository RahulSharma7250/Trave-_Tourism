from datetime import datetime
from bson import ObjectId

def to_dict(obj):
    obj['_id'] = str(obj['_id'])  # Convert ObjectId to string
    return obj

class User:
    collection = 'users'

    @staticmethod
    def create(mongo, user_data):
        mongo.users.insert_one(user_data)

    @staticmethod
    def find_by_email(mongo, email):
        return mongo.users.find_one({'email': email})

class Destination:
    collection = 'destinations'

    @staticmethod
    def get_all(mongo):
        return list(mongo.destinations.find())

    @staticmethod
    def get_by_id(mongo, destination_id):
        return mongo.destinations.find_one({'_id': ObjectId(destination_id)})

class Booking:
    collection = 'bookings'

    @staticmethod
    def create(mongo, booking_data):
        mongo.bookings.insert_one(booking_data)

    @staticmethod
    def get_by_user(mongo, user_id):
        return list(mongo.bookings.find({'user_id': user_id}))
