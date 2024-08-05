# Generated by Django 5.0.2 on 2024-08-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro_autor_livro_coautor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="autor",
        ),
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]
