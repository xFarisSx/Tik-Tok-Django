# Generated by Django 4.1.5 on 2023-01-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0006_commentlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos'),
        ),
    ]
