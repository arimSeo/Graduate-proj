from django.urls import path
from .views import index, gamseong, main,main2,detail,test,end
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns=[
    path('', index, name="index"),
    path('gamseong/', gamseong, name="gamseong"),
    path('main/', main, name="main"),
    path('main2/',main2, name="main2"),
    path('test/',test, name="test"),
    path('detail/',detail, name="detail"),
    path('end/',end, name="end")
] + static(settings.MEDIA_URL, serve,document_root=settings.MEDIA_ROOT)