# Generated by Django 3.1.7 on 2021-04-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler_App', '0002_auto_20210427_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlmodel',
            name='sku',
            field=models.CharField(default='', max_length=10000),
        ),
    ]