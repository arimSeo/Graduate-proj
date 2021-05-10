from django.urls import path
from .views import index, gamseong, main, main2
from django.conf import settings

urlpatterns=[
    path('', index, name="index"),
    # path('gamseong/(?P<pk>[0-9]+)$', gamseong, name="gamseong"),
    path('gamseong/', gamseong, name="gamseong"),
    path('main/', main, name="main"),
    path('main2/',main2, name="main2")
]