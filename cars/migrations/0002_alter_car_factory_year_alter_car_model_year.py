# Generated by Django 5.1 on 2024-09-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
