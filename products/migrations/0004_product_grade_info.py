# Generated by Django 3.2.15 on 2022-10-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_imdb_rating_product_imdbrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='grade_info',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
