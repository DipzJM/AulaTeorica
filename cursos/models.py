from django.db import models

# Create your models here.
class professor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    fotografia = models.ImageField()
    numero = models.IntegerField()
    def __str__(self):
        return self.nome

class curso(models.Model):
    nome = models.CharField(max_length=200)
    professor = models.ForeignKey(professor,on_delete=models.CASCADE,related_name="cursos")
    alunos = models.ManyToManyField(Aluno,related_name="alunos")
    def __str__(self):
        return self.nome


