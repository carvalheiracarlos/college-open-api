from rest_framework.exceptions import PermissionDenied

from CollegeOpen.Disciplines.models import Discipline, DisciplineReviews
from CollegeOpen.Academic.models import Student

def create_discipline_reviews(user, discipline, message, score):
    if not Student.objects.get(id=user.student.id):
        raise PermissionDenied('Usuario não estudante')

    if not Discipline.objects.filter(id=discipline.id).filter(students__id=user.student.id):
        raise PermissionDenied('Estudante Não Matriculado')

    if DisciplineReviews.objects.filter(student=user.student.id):
        raise PermissionDenied('Estudante Já fez o Review dessa disciplina')

    else:
        student = Student.objects.get(id=user.student.id)
        data = {
            'student': student,
            'discipline': discipline,
            'message': message,
            'score': score,
        }

        return DisciplineReviews.objects.create(**data)

