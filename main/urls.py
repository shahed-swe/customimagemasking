from django.urls import path
from . import views

urlpatterns = [
    path('mask/', views.MainApi.as_view(), name="mainapi")
]
