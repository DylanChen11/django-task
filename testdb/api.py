
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentExistsSerializer, ScoreSerializer
from .models import Score

class ScoreView(APIView):
        
    def get(self, request):
        scores=Score.objects.all()
        serializer=ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentExistsSerializer(data=request.data)
        
        if serializer.is_valid():
            # create score obj
            Score.objects.create(student_id=serializer.data["id"], value=serializer.data["score"])
            result=int(serializer.data["score"])+1
            return Response({"success": True,"result": result}, status=status.HTTP_200_OK)
        return Response({"success": False,"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)