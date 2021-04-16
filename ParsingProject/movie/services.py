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

def main_parsing(resp, data):
    soap = BeautifulSoup(resp.text, "lxml")
    movieName = soap.find("div", {'class': "titleBar"}).find("h1")
    data["name"] = movieName.contents[0].strip().replace(u'\xa0', u'')
    movieDesc = soap.find("div", {"class": "summary_text"})
    data["desc"] = movieDesc.string.strip()
    movieGenre = soap.find("div", {"class": "subtext"})
    data["genre"] = ""
    movieRating = soap.find("span", {"itemprop": "ratingValue"})
    data["rating"] = float(movieRating.string)
    movieImg = soap.find("div", {"class": "poster"}).find("img").get("src")
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urlrst.urlopen(movieImg).read())
    img_temp.flush()
    data["photo"] = movieImg
    for i in movieGenre.contents:
        data["genre"] += i.string.strip()
    print(data)
    mov_check = None
    try:
        mov_check = Movie.objects.get(name=data["name"])
        return Response({"data": f"Movie named {mov_check} is already parsed!"})
    except Movie.DoesNotExist:
        movie = Movie.objects.create(name=data["name"], desc=data["desc"], genre=data["genre"], rating=data['rating'])
        movie.photo.save('image.png', File(img_temp))
        items_lst = []
        items_lst.append(data)
        with open(CSV, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Movie name", "Description", "Poster link", "Genre", "Rating"])
            for item in items_lst:
                writer.writerow([item['name'], item['desc'], item['photo'], item['genre'], item['rating']])
        return Response({"data": "OK"})