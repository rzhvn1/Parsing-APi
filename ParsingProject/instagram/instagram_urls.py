from django.urls import path
from .views import *

urlpatterns = [
    path('', InstagramView.as_view())
]