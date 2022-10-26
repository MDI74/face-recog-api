from django.urls import path
from .views import *

app_name ='facerecognition'

urlpatterns = [
    path('api/getOrganization', OrganizationListCreateAPIView.as_view()),
    path('api/getWorker', WorkerListCreateAPIView.as_view()),
    path('api/createPhoto', CreatePhoto.as_view()),
    path('startFaceid', start_faceid),
    path('', add_worker),
]
