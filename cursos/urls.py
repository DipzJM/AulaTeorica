from .import views
from django import path

urlpatterns={
    path("/aluno-path/<int:aluno_id>",views.aluno_view,name="aluno-url"),
    path("/edita-curso/<int:curso_id>",views.edita_curso,name="edita-curso"),
    path("/novo-curso",views.novo_curso,name="novo-curso"),
    path("/cursos",views.cursos_view,name="cursos"),
}