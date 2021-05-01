from django.urls import path
from .views import index, gamseong, main

urlpatterns=[
    path('', index, name="index"),
    path('gamseong/', gamseong, name="gamseong"),
    path('main/', main, name="main"),
]