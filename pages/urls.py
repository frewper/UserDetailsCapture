from django.urls import path

from .views import home_page_view
from .views import first_page_view

urlpatterns = [
    path("", home_page_view, name="home"),

    path("first/",first_page_view, name="first"),
]