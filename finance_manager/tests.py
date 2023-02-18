from django.test import TestCase
from models import User

class BaseTest(TestCase):
    def create_user(self):
        user = User.objects.create(
            email='test@mail.ru',
            number='89121545772',
            first_name='Paul',
            last_name='Komarov',
        )
        user.set_password('1234567*')
        self.assertTrue(user.save())