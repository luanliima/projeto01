from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno

def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})
