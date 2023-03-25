from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import descison
import numpy as np
import cv2
import requests
class GarbageDecisionAPI(APIView):
    
    def get(self):
        return Response("Backend test")
    
    
    def post(self, request):
        file = request.FILES['file']
        act_no = request.POST.get('act_no')
        file_bytes = np.fromstring(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
        image = cv2.resize(image,(224,224))
        result = descison.delay(image.tolist())
        
        up = {'file':(file.name, file, "multipart/form-data")}
        data = {
            'category': result.get(),
            'act_no': act_no
        }
        server = requests.post('http://localhost:8080/api/v1/gcs',files=up,data=data)
        
        return Response(server.text,status=200)