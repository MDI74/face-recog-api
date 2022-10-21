from django.db import models


#Модель для организаций
class Organization(models.Model):
    id_organization = models.IntegerField("Наименование организации", primary_key=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __int__(self):
        return self.id_organization


#Модель для сотрудников
class Worker(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_worker = models.IntegerField("Номер сотрудника", primary_key=True)
    photo = models.ImageField("Фотография сотрудника", upload_to='images/')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __int__(self):
        return '%s %s' % (self.organization, self.id_worker)


class Session(models.Model):
    photo = models.ImageField("Фотография сотрудника", upload_to='images_camera/')

    class Meta:
        verbose_name = 'Фото с камеры'
        verbose_name_plural = 'Фото с камеры'

    def __int__(self):
        return '%s' % self.photo


