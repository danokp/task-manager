# Generated by Django 4.2.1 on 2023-06-25 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tag',
            new_name='label',
        ),
    ]
