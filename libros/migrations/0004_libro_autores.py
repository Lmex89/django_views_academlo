# Generated by Django 2.2 on 2021-06-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(related_name='libros', to='libros.Autor'),
        ),
    ]
