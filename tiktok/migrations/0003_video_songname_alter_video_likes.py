# Generated by Django 4.1.5 on 2023-01-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0002_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='songname',
            field=models.CharField(default='No song', max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
