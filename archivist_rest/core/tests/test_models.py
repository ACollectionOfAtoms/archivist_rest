from django.test import TestCase

from ..models import User
from . import factories


class TestUser(TestCase):
    def test_user_can_be_created(self):
        factories.UserFactory()
        user = User.objects.get(email=factories.UserFactory.email)
        self.assertIsNotNone(user)
