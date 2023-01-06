from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member/', views.addMember, name='add-member'),
    path('edit-member/<str:pk>', views.editMember, name='edit-member'),
    path('delete/<str:pk>', views.deleteMember, name='delete'),
]