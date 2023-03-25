
import datetime
import json

from django.urls import reverse
from rest_framework.test import APITestCase
from testdb.models import Score

from testdb.tests.factories import TeacherFactory, StudentFactory, ScoreFactory

class TestGetScoreView(APITestCase):

    GET_SCORE_URI=reverse("get-score")

    def setUp(self):
        self.student1=StudentFactory(id=1)
        self.student2=StudentFactory(id=2)
        self.teacher=TeacherFactory()
        self.score1=ScoreFactory(student=self.student1, value=50)
        self.score2=ScoreFactory(student=self.student1, value=90)

    def test_get_students_score(self):
        resp = self.client.get(self.GET_SCORE_URI)
        resp_json = resp.json()
        assert len(resp_json) ==2
        assert {"value": self.score1.value, "student": self.score1.student.id} in resp_json
        assert {"value": self.score2.value, "student": self.score2.student.id} in resp_json

    def test_get_score_success(self):
        response = self.client.post(
                    self.GET_SCORE_URI,
                    {
                        "id": self.student1.id,
                        "score": 40,
                    },
                )
        assert response.status_code == 200
        resp_json = response.json()

        # check the the result is score + 1
        assert resp_json["result"] == 41

        # check that score object is created
        score = Score.objects.last()
        assert score.student.id == self.student1.id
        assert score.value == 40
        
    
    def test_get_score_error(self):
        response = self.client.post(
                self.GET_SCORE_URI,
                {
                    "id": 999,
                    "score": 40,
                },
            )
        assert response.status_code == 400
        resp_data=json.loads(response.content.decode("utf8"))
        assert resp_data["success"] is False
        assert resp_data["error"] == {'id': ['Student with id does not exist']}