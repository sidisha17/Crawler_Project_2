# Generated by Django 3.1.7 on 2021-04-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='sku',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
