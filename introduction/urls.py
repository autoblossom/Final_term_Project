from django.urls import path
from .import views

app_name="introduction"

urlpatters=[
    path('',views.index,name="index"),
]