from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "Shop Home"),
    path("about", views.about, name = "About Us"),
    path("contact", views.contact, name = "Contact Us"),
    path("tracker", views.track, name = "Tracking Status"),
    path("search", views.search, name = "Search"),
    path("productview", views.prodView, name = "View Product"),
    path("checkout", views.checkOut, name = "Checkout"),
]