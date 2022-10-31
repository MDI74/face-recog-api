from .models import Worker, Session
from django.forms import ModelForm


#Класс формы для сотрудников
class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ["organization", "photo"]


# Класс формы для сотрудников
class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'