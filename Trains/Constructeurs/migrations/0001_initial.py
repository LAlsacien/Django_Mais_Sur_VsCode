# Generated by Django 4.0.4 on 2022-05-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constructeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('siege_social', models.CharField(max_length=100)),
                ('pays_origine', models.CharField(max_length=100)),
                ('date_creation', models.CharField(blank=True, max_length=4, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
