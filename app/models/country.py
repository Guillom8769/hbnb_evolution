from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()

class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.code, 'Country')

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(code):
        data = storage.get(code, 'Country')
        if data:
            country = Country(code=data['code'], name=data['name'])
            country.created_at = datetime.fromisoformat(data['created_at'])
            country.updated_at = datetime.fromisoformat(data['updated_at'])
            return country
        return None

    @staticmethod
    def get_all():
        data = storage.get_all('Country')
        countries = []
        for item in data:
            country = Country(code=item['code'], name=item['name'])
            country.created_at = datetime.fromisoformat(item['created_at'])
            country.updated_at = datetime.fromisoformat(item['updated_at'])
            countries.append(country)
        return countries

    @staticmethod
    def preload_data():
        countries = [
            {"code": "FR", "name": "France"},
            {"code": "US", "name": "United States"},
            # Ajoutez d'autres pays selon vos besoins
        ]
        for country_data in countries:
            country = Country(code=country_data['code'], name=country_data['name'])
            country.save()
