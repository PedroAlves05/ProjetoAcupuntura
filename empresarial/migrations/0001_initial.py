# Generated by Django 4.2.6 on 2023-11-18 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0003_exames_duracao'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutrasRegioes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hipotálamo', models.BooleanField(default=False)),
                ('Sacro', models.BooleanField(default=False)),
                ('Ponto_de_muro', models.BooleanField(default=False)),
                ('Cóccix', models.BooleanField(default=False)),
                ('Cervical', models.BooleanField(default=False)),
                ('Hipófise', models.BooleanField(default=False)),
                ('Torácica', models.BooleanField(default=False)),
                ('Pineal', models.BooleanField(default=False)),
                ('Lombar', models.BooleanField(default=False)),
                ('adrenal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PontosTratados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Olho', models.BooleanField(default=False)),
                ('Olfativo', models.BooleanField(default=False)),
                ('Mandibular', models.BooleanField(default=False)),
                ('Pulmões', models.BooleanField(default=False)),
                ('Auditivo', models.BooleanField(default=False)),
                ('Estômago', models.BooleanField(default=False)),
                ('Garganta', models.BooleanField(default=False)),
                ('Gônadas', models.BooleanField(default=False)),
                ('Pâncreas', models.BooleanField(default=False)),
                ('Coração', models.BooleanField(default=False)),
                ('Fígado', models.BooleanField(default=False)),
                ('Retal', models.BooleanField(default=False)),
                ('Ciático', models.BooleanField(default=False)),
                ('Joelho', models.BooleanField(default=False)),
                ('Rim', models.BooleanField(default=False)),
                ('Trigêmeo', models.BooleanField(default=False)),
                ('Agressividade', models.BooleanField(default=False)),
                ('Tragus', models.BooleanField(default=False)),
                ('Pele', models.BooleanField(default=False)),
                ('Ombro', models.BooleanField(default=False)),
                ('Zero', models.BooleanField(default=False)),
                ('M_inferiores', models.BooleanField(default=False)),
                ('M_superiores', models.BooleanField(default=False)),
                ('Alergia', models.BooleanField(default=False)),
                ('Darwin', models.BooleanField(default=False)),
                ('Síntese', models.BooleanField(default=False)),
                ('Tálamo', models.BooleanField(default=False)),
                ('Occipital', models.BooleanField(default=False)),
                ('Genital', models.BooleanField(default=False)),
                ('Medular', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontosUsados', models.CharField(max_length=1000)),
                ('Pagamento', models.BooleanField(default=False)),
                ('OutraRegião', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresarial.outrasregioes')),
                ('PontoTratado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresarial.pontostratados')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendamentos.agendarexame')),
            ],
        ),
    ]
