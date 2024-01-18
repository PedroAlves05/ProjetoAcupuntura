# Generated by Django 4.2.6 on 2023-11-18 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresarial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimentos',
            name='OutraRegião',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='empresarial.outrasregioes'),
        ),
        migrations.AlterField(
            model_name='procedimentos',
            name='PontoTratado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='empresarial.pontostratados'),
        ),
        migrations.AlterField(
            model_name='procedimentos',
            name='pontosUsados',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
