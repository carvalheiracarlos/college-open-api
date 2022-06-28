from django.db import transaction
from django.contrib.auth.models import User
from CollegeOpen.Academic.models import Student 


def get_from_user(user_id, Model):
    return Model.objects.get_from_user(user_id)


def user_create(username, email, password):
    username = username if username is not None else email
    return User.objects.create_user(username, email, password)


@transaction.atomic
def create(user, name, registration, Model):
    username = user['username'] if 'username' in user else user['email']
    user_entity = user_create(username or None, user['email'], user['password'])

    data = {
        'name': name,
        'user': user_entity,
        'registration': registration,
    }

    return Model.objects.create(**data)