# Generated by Django 4.1 on 2025-02-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='image', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
