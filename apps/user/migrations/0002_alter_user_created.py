# Generated by Django 4.0.4 on 2022-04-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
