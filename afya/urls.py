from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='index'),
    path('hospital/doctor_dashboard/', views.doctor_dashboard_view,name='doctor_dashboard'),
    path('hospital/doctor_patient/', views.doctor_patient_view, name='doctor_patient'),
    # path('auth/register/', views.register_user,name='register'),
    # path('profile/', views.profile,name='profile'),
    # path('project/<project_id>', views.project,name='project'),
    # path('api/profiles/', views.ProfileList.as_view()),
    # path('api/projects/', views.ProjectsList.as_view())
]