from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib import messages # type: ignore # mensagens de erro 
# Retornando uma página html
def home(request):
    if request.method=="POST": # Se o método request for post, valide login e senha, se não retorne a página home.
        username=request.POST['usuario']
        password=request.POST['senha']
        #Autenticação
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None: # condição após a validação
            login(request,user)
            messages.success(request,"Login realizado com sucesso!") # mensagem de confirmação de login
            return redirect('home')
        else:
            messages.error(request,"Erro na autenticação. Tente novamente!") # mensagem de erro de login
            return redirect('home')

    else:
        return render(request,'home.html') 


def logout_user(request):
    logout(request)
    messages.success(request, "Logout com sucesso!")
    return redirect('home')



def register_user(request):
    return render(request,"register.html")