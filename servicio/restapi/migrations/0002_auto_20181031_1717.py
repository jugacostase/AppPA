# Generated by Django 2.1.2 on 2018-10-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id_tarea', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('tarjeta', models.CharField(max_length=500)),
                ('tablero', models.CharField(max_length=500)),
                ('estado_tarjeta', models.CharField(max_length=500)),
                ('porcentaje_avance', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='Persona',
            new_name='correo',
        ),
    ]
