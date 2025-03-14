from django.urls import path
from django.http import HttpResponse
from livraria.views import home, sobre, logout_user


urlpatterns=[
    path('', home, name='home'), # Utiliza-se name para chamar a rota através do link
    path('sobre/', sobre),
    path('logout/',logout_user, name='logout')

]