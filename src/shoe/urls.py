from django.urls import path
from . import views

app_name = 'shoe'

urlpatterns = [
    path('', views.shoe_list, name='shoe_list'),
    path('liked_list', views.liked_list, name="liked_list"),
    path('cart_list', views.cart_list, name="cart_list"),
   	path('gender_male', views.gender_male, name="gender_male"),
   	path('gender_female', views.gender_female, name="gender_female"),

]