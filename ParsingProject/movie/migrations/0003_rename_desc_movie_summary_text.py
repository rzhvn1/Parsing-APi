# Generated by Django 3.2 on 2021-04-09 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='desc',
            new_name='summary_text',
        ),
    ]