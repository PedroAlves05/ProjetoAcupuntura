from django.db import models
from agendamentos.models import AgendarExame


# Create your models here.



class Procedimentos(models.Model):
    procedimento = models.ForeignKey(AgendarExame, on_delete=models.DO_NOTHING)
    pontosUsados = models.CharField(max_length=1000, default=None)
    Olho = models.BooleanField(default=False)
    Olfativo = models.BooleanField(default=False)
    Mandibular = models.BooleanField(default=False)
    Pulmões = models.BooleanField(default=False)
    Auditivo = models.BooleanField(default=False)
    Estômago = models.BooleanField(default=False)
    Garganta = models.BooleanField(default=False)
    Gônadas = models.BooleanField(default=False)
    Pâncreas = models.BooleanField(default=False)
    Coração = models.BooleanField(default=False)
    Fígado = models.BooleanField(default=False)
    Retal = models.BooleanField(default=False)
    Ciático = models.BooleanField(default=False)
    Joelho = models.BooleanField(default=False)
    Rim = models.BooleanField(default=False)
    Trigêmeo = models.BooleanField(default=False)
    Agressividade = models.BooleanField(default=False)
    Tragus = models.BooleanField(default=False)
    Pele = models.BooleanField(default=False)
    Ombro = models.BooleanField(default=False)
    Zero = models.BooleanField(default=False)
    M_inferiores = models.BooleanField(default=False)
    M_superiores = models.BooleanField(default=False)
    Alergia = models.BooleanField(default=False)
    Darwin = models.BooleanField(default=False)
    Síntese = models.BooleanField(default=False)
    Tálamo = models.BooleanField(default=False)
    Occipital = models.BooleanField(default=False)
    Genital = models.BooleanField(default=False)
    Medular = models.BooleanField(default=False)

    Hipotálamo = models.BooleanField(default=False)
    Sacro = models.BooleanField(default=False)
    Ponto_de_muro = models.BooleanField(default=False)
    Cóccix = models.BooleanField(default=False)
    Cervical = models.BooleanField(default=False)
    Hipófise = models.BooleanField(default=False)
    Torácica = models.BooleanField(default=False)
    Pineal = models.BooleanField(default=False)
    Lombar = models.BooleanField(default=False)
    adrenal = models.BooleanField(default=False)
    Pagamento = models.BooleanField(default=False)

    def __str__(self):
        return f"Procedimento para {self.procedimento}"



class Gastos(models.Model):
    novoGasto = models.CharField(max_length=300)
    valorGasto = models.FloatField()
    dataGasto = models.DateField()

