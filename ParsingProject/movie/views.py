import urllib.request as urlrst
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from bs4 import BeautifulSoup
from .serializers import MovieSerializer
import requests as rst
from .models import Movie
import csv
from ParsingProject.settings import CSV
from .services import main_parsing
#view that has func post
# {
# "url":["https://www.imdb.com/title/tt7888964/", "https://www.imdb.com/title/tt9419056/"]
# }
class MovieView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = {}
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            url_list = serializer.data.get('url')
            for url in url_list:
                resp = rst.get(url)
                main_parsing(resp,data)
            return Response({"data": "OK"})
        return Response(serializer.errors)



