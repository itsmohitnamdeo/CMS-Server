from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('courses/delete/<int:pk>/', views.CourseDelete.as_view(), name='course-delete'),
    path('instances/', views.CourseInstanceList.as_view(), name='instance-list'),
    path('instances/<int:pk>/', views.CourseInstanceDetail.as_view(), name='instance-detail'),
    path('instances/create/', views.CourseInstanceCreate.as_view(), name='instance-create'),
    path('instances/delete/<int:pk>/', views.CourseInstanceDelete.as_view(), name='instance-delete'),
    path('instances/<int:year>/<int:semester>/', views.CourseInstancesByYearSemester.as_view(), name='course-instances-year-semester'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', views.CourseInstanceDetail.as_view(), name='course-instance-detail'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', views.CourseInstanceDelete.as_view(), name='course-instance-delete'),
]
