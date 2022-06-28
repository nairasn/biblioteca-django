from django.db import models
from datetime import date

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    descricao = models.TextField()
    ano_edicao = models.IntegerField(blank=True, null=True)
        
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Livro'
    
    