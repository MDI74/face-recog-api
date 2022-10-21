from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import cv2
from deepface import DeepFace


def home_page(request):
    worker = Worker.objects.all()
    return render(request, 'facerecognition/main.html', {'worker': worker})


#Функция для распознования лица
def face_recognition(request):
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
            cv2.imwrite('detect/facedetects.jpg', img)
            # try:
            #     result = DeepFace.verify(img1_path='detect/facedetects.jpg', img2_path='images/img5.jpg',
            #                              distance_metric=metrics[2], detector_backend='mtcnn', model_name="VGG-Face")
            #
            #     print("Личность подтверждена") if result['verified'] else print("Личность не подтверждена")
            # except:
            #     print("Лицо не обнаружено")

        cv2.imshow('VideoCamera', img_n)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        if cv2.waitKey(1) & 0xff == ord('c'):
            try:
                result = DeepFace.find(img_path='detect/facedetects.jpg', db_path='images',
                                       distance_metric=metrics[2], detector_backend=backends[3], model_name=models[0])
                print(result)
                home_page(result['identity'][0])
            except:
                print("Лицо не обнаружено")

    cap.release()
    cv2.destroyAllWindows()


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class CreatePhoto(APIView):

    def get(self, request, format=None):
        session = Session.objects.all()
        serializers = SessionSerializer(session, many=True)
        return Response(serializers.data)

    def post(self, request):
        session = Session.photo()
        serializers = SessionSerializer(data=session)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATERD)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)