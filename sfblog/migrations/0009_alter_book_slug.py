# Generated by Django 3.2.18 on 2023-03-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfblog', '0008_alter_book_sub_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]