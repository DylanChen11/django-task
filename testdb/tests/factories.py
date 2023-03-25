import factory
from testdb.models import Student, Teacher, Score

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student
    id = factory.Sequence(lambda n: n)
    age = factory.Sequence(lambda n: n)
    name = factory.Faker("name")

class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher
    age = factory.Sequence(lambda n: n)
    uid =factory.Sequence(lambda n: n)

class ScoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Score

    