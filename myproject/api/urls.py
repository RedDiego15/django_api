
from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
]
