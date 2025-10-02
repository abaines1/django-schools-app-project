from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    # School URLs
    path('SchoolListView/', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.SchoolUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='delete'),

    # Student URLs
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='update_student'),
]
