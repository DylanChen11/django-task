from django.urls import include, path
from .api import ScoreView

urlpatterns = [
    path(
        "get-score/",
        ScoreView.as_view(),
        name="get-score",
    ),
]
