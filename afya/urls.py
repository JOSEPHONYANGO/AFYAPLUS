from django.urls import path
from . import views

urlpatterns = [
    # path('',views.is_doctor, name='doctor'),
    path('', views.doctor_dashboard_view,name='dashboard'),
    # path('accounts/logout/', views.logout_user, name='logout'),
    # path('auth/register/', views.register_user,name='register'),
    # path('profile/', views.profile,name='profile'),
    # path('project/<project_id>', views.project,name='project'),
    # path('api/profiles/', views.ProfileList.as_view()),
    # path('api/projects/', views.ProjectsList.as_view())
]