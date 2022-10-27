from .models import Worker
from django.forms import ModelForm


#Класс формы для сотрудников
class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ["organization", "photo"]