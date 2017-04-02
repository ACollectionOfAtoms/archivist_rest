import factory

from .. import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = 'example-user'
    first_name = 'Johnny'
    last_name = 'Appleseed'
    email = 'johnnyapp@factory.com'
