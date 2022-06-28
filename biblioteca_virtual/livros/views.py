from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from .models import Livros

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=nome).first()

        if user: 
            return HttpResponse('Já existe esse usuário')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect(login)

def login(resquest):
    if resquest.method == "GET":
        return render(resquest, 'login.html')
    else:
        nome = resquest.POST.get('nome')
        senha = resquest.POST.get('senha')
        
        user= authenticate(username=nome, password=senha)
        if(user):
            return redirect(livros_cadastro)
        else:
            return HttpResponse('Email ou senha inválidos.')

def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Autenticado.')
    return HttpResponse('Você precisa estar logado!')

def biblioteca(request):
    lista_de_livros = Livros.objects.all()
    context = {
        'livros': lista_de_livros
        }
    
    if request.method == 'GET':
         # request, arquivo.html, context = {dicionario }
        return render (request,'biblioteca.html', context)
    

def livros_cadastro(request):
    if request.method == "GET":
        return render(request, 'livros_cadastro.html')
    else:
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        descricao = request.POST.get('descricao')
        ano_edicao = request.POST.get('ano_edicao')        
                
        livros = Livros.objects.filter(titulo=titulo).first()

        if livros: 
            return HttpResponse('Esse livro já foi cadastrado.')
        livros = Livros.objects.create(titulo=titulo, autor=autor, descricao=descricao, ano_edicao=ano_edicao)
        livros.save()
        return redirect(biblioteca)

def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Autenticado.')
    return HttpResponse('Você precisa estar logado!')



    