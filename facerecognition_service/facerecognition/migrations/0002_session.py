# Generated by Django 4.1.2 on 2022-10-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecognition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images_camera/', verbose_name='Фотография сотрудника')),
            ],
            options={
                'verbose_name': 'Фото с камеры',
                'verbose_name_plural': 'Фото с камеры',
            },
        ),
    ]