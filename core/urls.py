from django.urls import path
from .views import ListMembersView, AddMemberView, EditMemberView, DeleteMemberView

urlpatterns = [
    path('', ListMembersView.as_view(), name='list-members'),
    path('add-member/', AddMemberView.as_view(), name='add-member'),
    path('edit-member/<str:pk>', EditMemberView.as_view(), name='edit-member'),
    path('delete-member/<str:pk>',DeleteMemberView.as_view(), name='delete-member'),
]