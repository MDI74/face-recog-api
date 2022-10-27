from django.urls import path
from .views import *

app_name ='facerecognition'

urlpatterns = [
    path('api/getOrganization', OrganizationListCreateAPIView.as_view()), #Добавления организаций через api
    path('api/getWorker', WorkerListCreateAPIView.as_view()), #Добавления сотрудников через api
    path('api/createPhoto', CreatePhotoListCreateAPIView.as_view()),
    path('startFaceid', start_faceid), #Запуск распознования лица
    path('', add_worker), #Добавления сотрудника через форму
]
