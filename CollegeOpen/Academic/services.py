from django.db import transaction
from django.contrib.auth.models import User
from CollegeOpen.Academic.models import Academic


def get_from_user(user_id):
    return Academic.objects.get_from_user(user_id)


def user_create(username, email, password):
    username = username if username is not None else email
    return User.objects.create_user(username, email, password)


@transaction.atomic
def create(user, name, registration):
    username = user['username'] if 'username' in user else user['email']
    user_entity = user_create(username or None, user['email'], user['password'])

    academic_data = {
        'name': name,
        'user': user_entity,
        'registration': registration,
        'is_professor': False
    }

    return Academic.objects.create(**academic_data)