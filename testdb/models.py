from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    uid=models.IntegerField(unique=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.uid)
    
class Score(models.Model):
    # subject = models.CharField(max_length=30, blank=True, null=True)
    value = models.PositiveIntegerField()
    student=models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="score_sets"
    )

    def __str__(self):
        return '{}, {}'.format(self.value, self.student.name)