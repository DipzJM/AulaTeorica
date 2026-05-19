from django.shortcuts import render,redirect
from .models import Curso,Aluno,Professor
from .forms import CursoForm

# Create your views here.
def cursos_view(request):
    context = {
        'cursos' : Curso.Objects.all()
    }
    return render(request,"/templates/Cursos/cursos.html",context)

def professores_view(request):
    context={
        'professores':Professor.Objects.all()
    }
    return render(request,"/templates/Professores/professores.html",context)



def aluno_view(request, aluno_id):
    context = {'aluno':Aluno.Objects.get(id = aluno_id)}
    return render(request,"templates/Alunos/aluno.html",context)

def novo_curso(request):
    
    form = CursoForm(request.POST or None)    
    
    if request.POST:
        if form.is_valid:
            form.save()
            return redirect("cursos")

    context ={
        'form' : form
    }
    return render(request,"cursos/novo-curso",context)
    

def edita_curso(request,curso_id):
    curso = Curso.Objects.get(id=curso_id)
    form = CursoForm(request.POST or None,instance=curso)    
    
    if request.POST:
        if form.is_valid:
            form.save()
            return redirect("cursos")

    context ={
        'form' : form,
        'curso_id' : curso_id
    }
    return render(request,"cursos/novo-curso",context)