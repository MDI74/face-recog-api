from rest_framework import generics
from .models import *
from django.shortcuts import render
from .serializers import *
from django.views.generic import CreateView
from deepface import DeepFace
from .forms import WorkerForm
from django.core.files.storage import FileSystemStorage
# class Detect(generics.ListCreateAPIView):
#     print("HI")
#     DeepFace.stream(db_path="C:/User/demon/Desktop/database")


def home_page(request):
    error = ' '
    if request.method == 'POST':
        form = WorkerForm(request.POST) #Создает объект на основе класса FeedbackForm
        if form.is_valid():
            form.save()
        else:
            error = "Введены некорректные данные"

    form = WorkerForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'facerecognition/main.html', context)


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
