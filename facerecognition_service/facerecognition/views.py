from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from deepface import DeepFace
from .forms import WorkerForm
import threading
import numpy as np
import cv2
from django.views.decorators import gzip



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def home_page(request):
    error = ' '
    if request.method == 'POST':
        form = WorkerForm(request.POST)
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


#Получение фото из базы данных
class WorkerPhotoListView(generics.ListAPIView):
    photo = Worker.objects.get(worker_id = 1).photo
    print(photo)
    # req = requests.get('http://' + photo)


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
