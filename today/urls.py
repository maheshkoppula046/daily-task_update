from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('unauthorized/', views.unauthorized_access, name='unauthorized_access'),
    path('upload-task/', views.upload_task, name='upload_task'),
    path('task-list/', views.task_list, name='task_list'),
    path('edit-task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete_task'),
]
