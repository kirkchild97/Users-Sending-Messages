from flask_app.config.mysqlconnection import connectToMySQL as connect

class Message:
    def __init__(self, data) -> None:
        self.sent_by = data['sent_by']
        self.sent_to = data['sent_to']
        self.content = data['content']

    @classmethod
    def send_message(cls, data):
        # Data should already be validated in the user before getting here
        pass