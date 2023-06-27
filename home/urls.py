from django.urls import path, include
from Views import *

urlpatterns=[
    path('', HomeView.as_view(), new='home'),

]