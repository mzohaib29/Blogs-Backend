# Generated by Django 4.2.2 on 2023-07-18 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiBase', '0003_user_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]
