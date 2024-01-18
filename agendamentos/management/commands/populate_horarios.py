from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from agendamentos.models import Horario

class Command(BaseCommand):
    help = 'Popula a tabela de Horarios com uma grande quantidade de horários.'

    def handle(self, *args, **options):
        # Data inicial
        data_inicial = datetime.now().date()

        # Número de dias para adicionar horários
        numero_de_dias = 15

        # Intervalo de tempo entre horários (em minutos)
        intervalo_de_tempo = 15

        for dia in range(numero_de_dias):
            data = data_inicial + timedelta(days=dia)
            
            # Verifica se o dia é sábado (5) ou domingo (6)
            if data.weekday() in [5, 6]:
                disponivel = False
            else:
                disponivel = True

            hora = datetime(data.year, data.month, data.day, 13, 0)  # Começa às 9:00 da manhã
            while hora.time() < datetime(data.year, data.month, data.day, 18, 0).time():  # Termina às 18:00
                # Define disponível como False se o horário estiver entre 12:00 e 13:00
                if not Horario.objects.filter(data=data, hora=hora.time()).exists():
                    if (hora.time() >= datetime(data.year, data.month, data.day, 12, 0).time() and \
                    hora.time() < datetime(data.year, data.month, data.day, 13, 0).time()) or data.weekday() in [5, 6]:
                        disponivel = False
                    else:
                        disponivel = True
                    Horario.objects.create(data=data, hora=hora.time(), disponivel=disponivel)
                hora += timedelta(minutes=intervalo_de_tempo)


        
        self.stdout.write(self.style.SUCCESS('Horários foram adicionados com sucesso.'))