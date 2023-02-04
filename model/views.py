from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import descison
import numpy as np
import cv2

class GarbageDecisionAPI(APIView):
    
    def get(self):
        return Response("Backend test")
    
    
    def post(self, request):
        file = request.FILES['id'].read()
        file_bytes = np.fromstring(file, np.uint8)
        image = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
        image = cv2.resize(image, (224,224))
        result = descison.delay(image.tolist())
        
        return Response(result.get(),status=200)

