from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('',views.home,name="index"),
    path('dash/',views.dash,name="dash"),
    path('review/',views.review,name="review"),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    
    path('<str:a>/',views.notfo,name="notfound")
]