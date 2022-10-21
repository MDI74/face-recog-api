from django.urls import path
from .views import *
from django.http import StreamingHttpResponse


app_name ='facerecognition'

urlpatterns = [
    # path('detect', Detect.as_view()),
    path('getOrganization', OrganizationListCreateAPIView.as_view()),
    path('getWorker', WorkerListCreateAPIView.as_view()),
    path('createPhoto', CreatePhoto.as_view()),
    path('', home_page),
    path('face', face_recognition)

]
