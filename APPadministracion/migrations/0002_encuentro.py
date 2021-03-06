# Generated by Django 3.2.3 on 2021-08-22 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPadministracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuentro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreA', models.CharField(max_length=30)),
                ('nombreB', models.CharField(max_length=30)),
                ('fechaPartido', models.DateField(verbose_name='(ddd/mmm/yyy)')),
                ('hora', models.CharField(max_length=10)),
                ('golesA', models.IntegerField(default=0)),
                ('golesB', models.IntegerField(default=0)),
                ('faltas', models.IntegerField(default=0)),
                ('tarjetaRoja', models.IntegerField(default=0)),
                ('tarjetaAmarilla', models.IntegerField(default=0)),
                ('PropiedadTorneo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='APPadministracion.torneo')),
            ],
        ),
    ]
