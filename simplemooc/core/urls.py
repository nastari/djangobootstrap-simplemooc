from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homeDefault ),
]


# A URL quer a VIEWS importada. 