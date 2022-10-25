from django.urls import path
from .views import *


app_name ='facerecognition'

urlpatterns = [
    path('getOrganization', OrganizationListCreateAPIView.as_view()),
    path('getWorker', WorkerListCreateAPIView.as_view()),
    path('createPhoto', CreatePhoto.as_view()),
    path('', home_page),
]
