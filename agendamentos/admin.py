from django.contrib import admin
from .models import Horario, Exames, AgendarExame

# Register your models here.

admin.site.register(Horario)
admin.site.register(Exames)
admin.site.register(AgendarExame)
