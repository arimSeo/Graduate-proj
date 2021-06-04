from django.urls import path
from .views import index, gamseong, main, main2,test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', index, name="index"),
    path('gamseong/', gamseong, name="gamseong"),
    # path('gamseong/<int:pk>', gamseong, name="gamseong"),
    path('main/', main, name="main"),
    path('main2/',main2, name="main2"),
    path('test/',test, name="test")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)