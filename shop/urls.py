from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/product', views.index, name="products"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contactUs"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('product/<int:myid>', views.productview, name="productview"),
    path('checkout/', views.checkout, name="checkout"),
]
