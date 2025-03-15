from django.urls import path
from django.http import HttpResponse
from livraria.views import home, register_user, logout_user


urlpatterns=[
    path('', home, name='home'), # Utiliza-se name para chamar a rota através do link
    path('register/', register_user, name='register'),
    path('logout/',logout_user, name='logout')

]