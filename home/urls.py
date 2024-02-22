from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('create-task/',views.create_task,name='create_task'),
    path('delete-task/<int:id>',views.delete_task,name="delete_task"),
    path('update-task/<int:id>',views.update_task,name="update_task"),

]