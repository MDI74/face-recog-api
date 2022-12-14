from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from .forms import *
import cv2
from deepface import DeepFace

metrics = ["cosine", "euclidean", "euclidean_l2"]

models = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
]

backends = [
    'opencv',
    'ssd',
    'dlib',
    'mtcnn',
    'retinaface',
    'mediapipe'
]


#Функция для запуска распознования лица
def start_faceid(request):
    upload_photo()
    form = WorkerForm()
    return render(request, 'facerecognition/main.html', {'form': form})


#Функция для загрузки в базу данных фото с камеры
def upload_photo():
    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    if not os.path.isdir('session_image'):
        os.mkdir('session_image')
    while True:
        res, img = cap.read()

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_n = img.copy()
        faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

        for (x, y, w, h) in faces:
            cv2.rectangle(img_n, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.imwrite('detect/facedetect.jpg', img[y:y + h, x:x + w])
            cv2.imwrite('session_image/facedetects.jpg', img)

        cv2.imshow('VideoCamera', img_n)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    photo = Session()
    photo.photo = 'session_image/facedetects.jpg'
    photo.save()
    face_recognition()


#Функция для распознования лица
def face_recognition():
    id = 1
    model = DeepFace.build_model('VGG-Face')
    worker = Worker
    result = DeepFace.find(img_path='session_image/facedetects.jpg', db_path=f'images{id}',
                           distance_metric=metrics[2], detector_backend=backends[3],  model=model)
    print(result)
    try:
        if result['identity'][0]:
            res = worker.objects.filter(photo=result['identity'][0]) #Получаем id организации и сотрудника
            print('Найденное совпадение в базе данных ->', res[0])
    except:
        print("Личность в базе данных не найдена")
    session = Session.objects.all()
    session.delete()


#Функция для добавления сотрудников через форму
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        # form_s = SessionForm(request.POST, request.FILES)
        # if form_s.is_valid():
        #     form_s.save()
        if form.is_valid():
            form.save()
    else:
        form = WorkerForm()
        # form_s = SessionForm()
    return render(request, 'facerecognition/main.html', {'form': form})
    # return render(request, 'facerecognition/main.html', {'form': form, 'form_s' : form_s})


#Класс для добавления и вывода организаций в интерфейсе api
class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


#Класс для добавления и вывода сотрудников в интерфейсе api
class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Класс для добавления и вывода сессии в интерфейсе api
class CreatePhotoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
