from django.db import models

from django.shortcuts import get_object_or_404


class AcademicQueryset(models.QuerySet):

    def get_from_user(self, user_id):
        return get_object_or_404(self, user__id=user_id)