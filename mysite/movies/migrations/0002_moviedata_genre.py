# Generated by Django 2.2 on 2020-03-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
