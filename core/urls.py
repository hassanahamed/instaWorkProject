from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMembers, name='list-members'),
    path('add-member/', views.addMember, name='add-member'),
    path('edit-member/<str:pk>', views.editMember, name='edit-member'),
    path('delete-member/<str:pk>', views.deleteMember, name='delete-member'),
]