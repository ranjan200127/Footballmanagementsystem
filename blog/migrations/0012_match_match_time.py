# Generated by Django 3.1.2 on 2020-12-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201211_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_time',
            field=models.TimeField(default='5:30:30'),
        ),
    ]
