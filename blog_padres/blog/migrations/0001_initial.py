# Generated by Django 4.2.6 on 2023-11-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('subtitulo', models.CharField(max_length=256)),
                ('cuerpo', models.CharField(max_length=10000)),
                ('autor', models.CharField(max_length=256)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]