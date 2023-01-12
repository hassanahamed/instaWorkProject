from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import MemberForm
from .models import Member
from .appConstants import *

class ListMembersView(ListView):
    model = Member
    template_name = HOME_PAGE
    context_object_name = MEMBERS
    ordering = ORDER_BY_VALUE

class AddMemberView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = NEW_PAGE
    success_url = reverse_lazy(LIST_MEMBERS)


class EditMemberView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = EDIT_PAGE
    success_url = reverse_lazy(LIST_MEMBERS)

class DeleteMemberView(DeleteView):
    model = Member
    template_name = DELETE_PAGE
    success_url = reverse_lazy(LIST_MEMBERS)

class MemberDetailView(DetailView):
    model = Member
    template_name = HOME_PAGE

