# Generated by Django 5.2.2 on 2025-06-05 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='datetime',
            new_name='created_at',
        ),
    ]
