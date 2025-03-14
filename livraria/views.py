from django.shortcuts import render
from django.http import HttpResponse

# Retornando uma página html
def home(request):
    return render(request,'home.html') 


def logout_user(request):
    pass



def sobre(request):
    return HttpResponse('Teste Sobre')