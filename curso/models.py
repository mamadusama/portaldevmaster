from django.db import models
from django.utils import timezone


LISTA_CATEGORIAS_CURSOS = (
  ('DESENVOLVIMENTOWEB', 'Desenvolvimento Web'),
  ('ANALISEDEDADOS', 'Análise de Dados'),
  ('PROGRAMACAO', 'Programação'),
  ('BANCODEDADOS', 'Banco de Dados'),
  ('APRESENTACAO', 'Apresentação'),
  ('OUTROS', 'Outros'),
)

# criar curso
class Curso(models.Model):
  titulo = models.CharField(max_length=100)
  descricao= models.TextField(max_length=2000)
  imagem = models.ImageField(upload_to='imagens_cursos')
  data_criacao = models.DateTimeField(default=timezone.now) # default=timezone.now() hr em q aurso está sendo visto
  visualizacoes = models.PositiveIntegerField(default=0)
  categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIAS_CURSOS)
  avaliacao = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
  numero_aulas = models.PositiveIntegerField(default=0) 
  ativo = models.BooleanField(default=True) 
  destacado = models.BooleanField(default=False)
  data_atualizacao = models.DateTimeField(auto_now=True)
  quantidade_inscritos = models.PositiveIntegerField(default=0)



  def __str__(self):
      return f"{self.titulo} " # - {self.modulo.titulo}"







# criar Modulos


# Criar Usuarios