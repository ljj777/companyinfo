# Generated by Django 4.1.7 on 2023-02-26 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_complete_todo_complet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complet',
            new_name='complete',
        ),
    ]
