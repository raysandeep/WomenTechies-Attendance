from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('dash/',views.dash,name="dash"),
    path('review/',views.review,name="review")
]