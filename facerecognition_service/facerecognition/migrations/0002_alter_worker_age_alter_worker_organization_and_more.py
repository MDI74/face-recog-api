# Generated by Django 4.1.2 on 2022-10-17 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facerecognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facerecognition.organization'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.IntegerField(verbose_name='Номер сотрудника'),
        ),
    ]
