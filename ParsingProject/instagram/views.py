from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from .models import *
from .serializers import *
import requests as rst
from bs4 import BeautifulSoup
# Create your views here.

class InstagramView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = {}
        serializer = InstagramSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data.get('url')
            resp = rst.get(url)
            soap = BeautifulSoup(resp, 'lxml')
            postDesc = soap.find('div', {'class':'C4VMK'}).find('span').get('class')
            print(postDesc)
            data['post_desc'] = postDesc
            return Response({"data":"OK"})
        return Response(serializer.errors)


