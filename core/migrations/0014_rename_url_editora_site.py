# Generated by Django 5.1 on 2024-08-23 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_rename_site_editora_url_rename_autor_livro_autores_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="editora",
            old_name="url",
            new_name="site",
        ),
    ]
