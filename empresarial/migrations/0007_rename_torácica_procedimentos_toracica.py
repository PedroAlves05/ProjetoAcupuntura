# Generated by Django 4.2.6 on 2023-11-18 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresarial', '0006_remove_procedimentos_outras_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='procedimentos',
            old_name='Torácica',
            new_name='Toracica',
        ),
    ]
