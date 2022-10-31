import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


#Модель для организаций
class Organization(models.Model):
    id_organization = models.IntegerField("Номер организации", primary_key=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return str(self.id_organization)


#Функция для загрузки фотографий в папку в зависимости от организации
def image_upload_path(instance, filename):
    if not instance.organization:
        instance.save()
    if not os.path.isdir(f'images{instance.organization}'):
        os.mkdir(f'images{instance.organization}')
    directory = f'images{instance.organization}'
    db = os.listdir(directory)
    for item in db:
        if item.endswith(".pkl"):
            os.remove(os.path.join(directory, item))
    return f'images{instance.organization}/{filename}'


#Модель для сотрудников
class Worker(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_worker = models.AutoField("Номер сотрудника", primary_key=True)
    photo = models.ImageField("Фотография сотрудника", upload_to=image_upload_path)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '%s %s' % (str(self.organization), str(self.id_worker))


#Функция для удаления фото из папки вместе с удалением сотрудника из базы данных
@receiver(pre_delete, sender=Worker)
def worker_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    directory = f'images{instance.organization}'
    db = os.listdir(directory)
    for item in db:
        if item.endswith(".pkl"):
            os.remove(os.path.join(directory, item))


#Модель для сессии
class Session(models.Model):
    photo = models.ImageField("Фотография сотрудника", upload_to='session_image/')

    class Meta:
        verbose_name = 'Фото с камеры'
        verbose_name_plural = 'Фото с камеры'

    def __int__(self):
        return '%s' % self.photo


#Функция для удаления фото сделаного клиентом из папки вместе с удалением сессии из базы данных
@receiver(pre_delete, sender=Session)
def session_delete(sender, instance, **kwargs):
    instance.photo.delete(False)



