# Generated by Django 4.2.7 on 2023-12-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitarbeiter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitarbeiter',
            name='profilbild',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
