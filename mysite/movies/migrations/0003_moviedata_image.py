# Generated by Django 2.2 on 2020-03-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images/'),
        ),
    ]