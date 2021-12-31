from flask_app.config.mysqlconnection import connectToMySQL as connect
from flask_app.models.message import Message

class User:
    def __init__(self, data) -> None:
        self.user_id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_user_info(cls, data):
        pass

    @classmethod
    def get_messages(cls, data):
        pass

    @classmethod
    def get_sent_messages(cls, data):
        pass

    @classmethod
    def save_user(cls, data):
        pass

    @staticmethod
    def register_validation(data):
        pass

    @staticmethod
    def valid_user(data):
        pass

    @staticmethod
    def login_validation(data):
        pass