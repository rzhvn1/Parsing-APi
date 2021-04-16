# Generated by Django 3.2 on 2021-04-14 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PNC', to='instagram.comment')),
                ('post_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.instagram')),
            ],
        ),
    ]