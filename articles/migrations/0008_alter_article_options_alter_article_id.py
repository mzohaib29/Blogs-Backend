# Generated by Django 4.2.3 on 2023-07-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_author_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
