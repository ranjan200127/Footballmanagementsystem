# Generated by Django 3.1.2 on 2020-12-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201209_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='content',
            field=models.TextField(default='football player'),
        ),
    ]
