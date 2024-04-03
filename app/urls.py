from django.urls import path
from .views import *

urlpatterns = [
    path('', CalApp, name = 'CALCULATER'),
]