# Generated by Django 3.2 on 2021-04-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]
