from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Horario(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.data} - {self.hora}'


class Exames(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    duracao = models.TimeField(default='00:00')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class AgendarExame(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exame = models.ForeignKey(Exames, on_delete=models.DO_NOTHING)
    data = models.ForeignKey(Horario, on_delete=models.DO_NOTHING)
    cancelado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.usuario} | {self.exame.nome}'