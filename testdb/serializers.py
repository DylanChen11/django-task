from rest_framework import serializers
from .models import Student, Teacher, Score


class StudentSerializer(serializers.ModelSerializer):
    """
    Returns student information
    """

    class Meta:
        model = Student
        fields = ("name", "age")


class ScoreSerializer(serializers.ModelSerializer):
    """
    Returns score information
    """

    class Meta:
        model = Score
        fields = ("value", "student")

class StudentExistsSerializer(serializers.Serializer):
    """
    Checks if student exists in the system
    """

    id = serializers.IntegerField()
    score = serializers.IntegerField()


    def validate_id(self, id):
        if not Student.objects.filter(id=id).exists():
            raise serializers.ValidationError("Student with id does not exist")
        return id