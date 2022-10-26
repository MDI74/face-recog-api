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


#Функция для загрузки в базу данных фото с камеры
def upload_photo():
    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    while True:
        res, img = cap.read()

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_n = img.copy()
        faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

        for (x, y, w, h) in faces:
            cv2.rectangle(img_n, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.imwrite('detect/facedetect.jpg', img[y:y + h, x:x + w])
            cv2.imwrite('images_camera/facedetects.jpg', img)

        cv2.imshow('VideoCamera', img_n)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    photo = Session()
    photo.photo = 'images_camera/facedetects.jpg'
    photo.save()
    face_recognition()


#Функция для распознования лица
def face_recognition():
    worker = Worker
    result = DeepFace.find(img_path='images_camera/facedetects.jpg', db_path='images',
                           distance_metric=metrics[2], detector_backend=backends[3], model_name=models[0])
    print(result)
    try:
        if result['identity'][0]:
            res = worker.objects.filter(photo=result['identity'][0])
            print(res[0])
    except:
        print("Личность не найдена")
    session = Session.objects.all()
    session.delete()


#Функция для добавления сотрудников через форму
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            directory = "images/"
            db = os.listdir(directory)
            for item in db:
                if item.endswith(".pkl"):
                    os.remove(os.path.join(directory, item))
    else:
        form = WorkerForm()

    return render(request, 'facerecognition/main.html', {'form': form})


#Класс для добавления и вывода организаций в интерфейсе api
class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


#Класс для добавления и вывода сотрудников в интерфейсе api
class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Класс для добавления и вывода сессии в интерфейсе api
class CreatePhoto(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
