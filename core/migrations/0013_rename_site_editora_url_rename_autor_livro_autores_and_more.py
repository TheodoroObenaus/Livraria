# Generated by Django 5.1 on 2024-08-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_autor_options_alter_user_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="editora",
            old_name="site",
            new_name="url",
        ),
        migrations.RenameField(
            model_name="livro",
            old_name="autor",
            new_name="autores",
        ),
        migrations.AddField(
            model_name="editora",
            name="cidade",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
