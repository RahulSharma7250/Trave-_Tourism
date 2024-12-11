import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'rahul@123')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://userdata:data123@cluster0.wezvo.mongodb.net/travelerDatabase?retryWrites=true&w=majority&appName=Cluster0')
