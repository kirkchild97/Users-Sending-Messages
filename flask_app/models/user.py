from enum import Flag
from flask_app.config.mysqlconnection import connectToMySQL as connect
from flask_app.models.message import Message
from flask import flash
import re

class User:
    def __init__(self, data) -> None:
        self.user_id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_user_info(cls, data : dict):
        pass

    @classmethod
    def get_messages(cls, data : dict):
        pass

    @classmethod
    def get_sent_messages(cls, data : dict):
        pass

    @classmethod
    def save_user(cls, data : dict):
        pass

    @staticmethod
    def register_validation(data : dict):
        validator = {
            'is_valid' : True,
            'first_name' : 'First Name is not valid.',
            'last_name' : 'Last Name is not valid.',
            'email' : (re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'), 'Email is not valid'),
            'password' : 'Password is not valid or does not match.'
        }
        for set in data.items():
            if set[1] == None:
                flash('Please fill out all information.')
                validator['is_valid'] = False
            match set[0]:
                case 'first_name' | 'last_name':
                    if set[1].isspace() or len(set[1]) < 2:
                        flash(validator[set[0]])
                        validator['is_valid'] = False
                case 'email':
                    if not validator['email'][0].match(set[1]):
                        flash(validator['email'][1])
                        validator['is_valid'] = False
                case 'password':
                    if not set[1][0] == set[1][1] or len(set[1][0]) < 8:
                        flash(validator['password'])
                        validator['is_valid'] = False
                case _:
                    print('Unexpected parameter given.')
        return validator['is_valid']

    @staticmethod
    def valid_user(data : dict):
        pass

    @staticmethod
    def login_validation(data : dict):
        pass