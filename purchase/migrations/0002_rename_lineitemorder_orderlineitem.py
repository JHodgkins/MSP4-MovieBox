# Generated by Django 3.2.15 on 2022-09-22 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_imdb_rating_product_imdbrating'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineItemOrder',
            new_name='OrderLineItem',
        ),
    ]
