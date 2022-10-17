from .models import Worker
from django.forms import ModelForm


class WorkerForm(ModelForm):

    class Meta:
        model = Worker
        fields = '__all__'