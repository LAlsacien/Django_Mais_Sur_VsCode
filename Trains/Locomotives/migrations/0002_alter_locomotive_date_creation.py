# Generated by Django 4.0.4 on 2022-05-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locomotives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locomotive',
            name='date_creation',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]