# Generated by Django 4.1.2 on 2022-10-31 06:56

from django.db import migrations, models
import facerecognition.models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecognition', '0003_alter_organization_id_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(upload_to=facerecognition.models.image_upload_path, verbose_name='Фотография сотрудника'),
        ),
    ]
