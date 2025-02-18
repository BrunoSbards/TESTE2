from django.shortcuts import render
from .models import estado, matricula, leiloeiro

def home(request):
    leiloeiros = leiloeiro.objects.all()
    matriculas = matricula.objects.all()
    estados = estado.objects.all()
    return render (request, 'index.html',{"leiloeiros": leiloeiros})

def cadastro(request):
    vnome = request.POST.get("nome")
    vcpf = request.POST.get("cpf")
    vemail = request.POST.get("email")
    vtelefone = request.POST.get("telefone")
    vsite = request.POST.get("site")
    vmatricula = request.POST.get("matricula")
    leiloeiro.objects.create(nome=vnome)
    leiloeiro.objects.create(cpf=vcpf)
    leiloeiro.objects.create(email=vemail)
    leiloeiro.objects.create(telefone=vtelefone)
    leiloeiro.objects.create(site=vsite)
    matricula.objects.create(numero_matricula=vmatricula)
    leiloeiros = leiloeiro.objects.all()
    leiloeiros = matricula.objects.all()
    return render (request, 'index.html',{"leiloeiros": leiloeiros})

def editar(request, id):
    leiloeiro = leiloeiro.objects.get(id=id)
    return render (request, 'update.html', {'leiloeiro': leiloeiro})
