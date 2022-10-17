from django.db import models


class Organization(models.Model):
    name = models.CharField("Наименование организации", max_length=120, primary_key=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class Worker(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    age = models.IntegerField("Возраст", )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    worker_id = models.IntegerField("Номер сотрудника")
    photo = models.ImageField("Фотография сотрудника", upload_to='images/')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)
