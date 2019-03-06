# Generated by Django 2.1.7 on 2019-03-06 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='personalizacao',
            name='tempo',
            field=models.IntegerField(default=0, help_text='Tempo em minutos'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='personalizacao',
            field=models.ManyToManyField(blank=True, to='pizzaria.Personalizacao'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sabor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaria.Sabor'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaria.Tamanho'),
        ),
        migrations.AlterField(
            model_name='sabor',
            name='tempo',
            field=models.IntegerField(default=0, help_text='Tempo em minutos'),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='tempo',
            field=models.IntegerField(default=0, help_text='Tempo em minutos'),
        ),
    ]
