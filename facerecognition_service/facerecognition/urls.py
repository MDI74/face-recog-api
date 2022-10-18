from django.urls import path
from .views import *
from django.http import StreamingHttpResponse
app_name ='facerecognition'

urlpatterns = [
    # path('detect', Detect.as_view()),
    path('getOrganization', OrganizationListCreateAPIView.as_view()),
    path('getWorker', WorkerListCreateAPIView.as_view()),
    path('getPhoto', WorkerPhotoListView.as_view()),
    path('monitor', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                         content_type='multipart/x-mixed-replace; boundary=frame')),
    path('', home_page),

]
