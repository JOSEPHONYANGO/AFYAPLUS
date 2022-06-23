from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='index'),
    path('hospital/doctor_dashboard/', views.doctor_dashboard_view,name='hospital/doctor_dashboard.html'),
    path('hospital/doctor_patient/', views.doctor_patient_view, name='hospital/doctor_patient'),
    path('hospital/doctor_view_patient', views.doctor_view_patient_view, name='hospital/doctor_view_patient'),
    path('doctor_view_discharge_patient/', views.doctor_view_discharge_patient_view, name='hospital/doctor_view_discharge_patient'),
    path('hospital/doctor_appointment/', views.doctor_appointment_view, name='hospital/doctor_appointment'),
    path('hospital/doctor_view_appointment/', views.doctor_view_appointment_view, name='hospital/doctor_view_appointment'),
    path('hospital/doctor_delete_appointment/', views.doctor_delete_appointment_view, name='hospital/doctor_delete_appointment/'),
    
    # path('api/projects/', views.ProjectsList.as_view())
]