from django.urls import path
from . import views
urlpatterns = [
    path('project', views.Projects,name='project'),
    path('project_details', views.Projects_details,name='project_details'),
]