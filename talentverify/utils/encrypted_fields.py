# utils/encrypted_fields.py
from django.conf import settings
from cryptography.fernet import Fernet
from django.db import models

cipher = Fernet(settings.FERNET_KEY)

class EncryptedTextField(models.TextField):
    def get_prep_value(self, value):
        if value is None:
            return value
        return cipher.encrypt(value.encode()).decode()

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return cipher.decrypt(value.encode()).decode()

class EncryptedCharField(models.CharField):
    def get_prep_value(self, value):
        if value is None:
            return value
        return cipher.encrypt(value.encode()).decode()

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return cipher.decrypt(value.encode()).decode()
