from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()

class User:
    def __init__(self, email, password, first_name, last_name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.id, 'User')

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(user_id):
        data = storage.get(user_id, 'User')
        if data:
            user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
            user.id = data['id']
            user.created_at = datetime.fromisoformat(data['created_at'])
            user.updated_at = datetime.fromisoformat(data['updated_at'])
            return user
        return None

    @staticmethod
    def get_all():
        data = storage.get_all('User')
        users = []
        for item in data:
            user = User(email=item['email'], password=item.get('password', ''), first_name=item['first_name'], last_name=item['last_name'])
            user.id = item['id']
            user.created_at = datetime.fromisoformat(item['created_at'])
            user.updated_at = datetime.fromisoformat(item['updated_at'])
            users.append(user)
        return users
