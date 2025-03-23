from django.urls import path
from django.http import HttpResponse
from livraria.views import home, register_user, logout_user, book_detail, book_delete, book_add, book_update


urlpatterns=[
    path('', home, name='home'), # Utiliza-se name para chamar a rota através do link
    path('register/', register_user, name='register'),
    path('logout/',logout_user, name='logout'),
    path('book/<int:id>',book_detail,name='book'),
    path('delete_book/<int:id>',book_delete,name='delete_book'),
    path('add_book/', book_add, name='add_book'),
    path('update_book/<int:id>', book_update, name='update_book')

]