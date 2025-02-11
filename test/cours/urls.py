from django.urls import path
from . import views

app_name = "cours"

urlpatterns = [
    path('', views.CoursListView.as_view(), name="cours_list"),
    path('', views.CoursCreateView.as_view(), name="cours_create"),
    path('', views.LessonListView.as_view(), name="lesson_list"),
    path('<int:pk>/', views.cours_detail, name='cours_detail')
]
