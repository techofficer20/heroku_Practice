from django.urls import path
from . import views
urlpatterns = [
    path('', views.portfolio, name = "portfolio"),
    path('upload/', views.upload, name = "upload"),
    path('file_upload/', views.file_upload, name='file_upload'),
]