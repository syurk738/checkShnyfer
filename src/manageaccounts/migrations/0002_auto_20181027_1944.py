# Generated by Django 2.1.1 on 2018-10-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]