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


#Модель для сотрудников
class Worker(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_worker = models.IntegerField("Номер сотрудника", primary_key=True)
    photo = models.ImageField("Фотография сотрудника", upload_to='images/')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '%s %s' % (str(self.organization), str(self.id_worker))


#Функция для удаления фото из папки вместе с удалением сотрудника из базы данных
@receiver(pre_delete, sender=Worker)
def worker_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    directory = "images/"
    test = os.listdir(directory)
    for item in test:
        if item.endswith(".pkl"):
            os.remove(os.path.join(directory, item))


class Session(models.Model):
    photo = models.ImageField("Фотография сотрудника", upload_to='images_camera/')

    class Meta:
        verbose_name = 'Фото с камеры'
        verbose_name_plural = 'Фото с камеры'

    def __int__(self):
        return '%s' % self.photo

# #Функция для удаления фото с камеры  из папки вместе с удалением сессии из базы данных
# @receiver(pre_delete, sender=Session)
# def session_delete(sender, instance, **kwargs):
#     instance.photo.delete(False)
#


