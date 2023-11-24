from django.urls import path
from .views import *

urlpatterns = [
    path('country/', CountryView.as_view()),
]