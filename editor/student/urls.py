from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='student_dashboard'),
    path('test', views.test, name='test')
]