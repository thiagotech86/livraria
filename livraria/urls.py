from django.urls import path
from django.http import HttpResponse
from livraria.views import home, sobre


urlpatterns=[
    path('', home, name='home'), # Utiliza-se name para chamar a rota através do link
    path('sobre/', sobre)

]