# from django.core.exceptions import ValidationError
# from django.shortcuts import render, redirect
# from .team_management_exception import TeamManagementFacadeException
# from .forms import MemberForm
# from .models import Member, Role
# from .mapper_config import MemberConfig
# from .appConstants import *


# member_config = MemberConfig()

# def listMembers(request):
#     """
#     View function to display a list of all members, with the option to search for members by name.
#     If a search query is provided, return a list of members whose first or last name match the search query.
#     Otherwise, return a list of all members.
#     """
#     members = Member.objects.all()
#     search_input = request.GET.get(SEARCH)
#     if search_input:
#         first_name_members = Member.objects.filter(first_name__icontains=search_input)
#         last_name_members = Member.objects.filter(last_name__icontains=search_input)
#         members = (first_name_members | last_name_members).distinct().order_by(ORDER_BY_VALUE)
#     else:
#         members = Member.objects.all().order_by(ORDER_BY_VALUE)
#         search_input = EMPTY_STRING
#     return render(request, INDEX_PAGE, {MEMBERS: members, SEARCH: search_input, MEMBER_COUNT: len(members)})

# def addMember(request):
#     """
#     View function to add a new member to the database.
#     On GET request, render the 'new member' form.
#     On POST request, validate and save the new member form.
#     """
#     data = member_config.get_data(request.POST)
#     new_member_form = MemberForm(data)
#     try:
#         if request.method == POST_METHOD:
#             if not new_member_form.is_valid():
#                 raise TeamManagementFacadeException(new_member_form.errors.get_json_data())
#             new_member = new_member_form.save(commit=False)
#             new_member.role = Role(request.POST.get(ROLE,DEFAULT_ROLE))
#             new_member.save()
#             return redirect(HOME_PAGE)

#         return render(request, NEW_PAGE, {MEMBER: EMPTY_STRING})
#     except TeamManagementFacadeException as e:
#         return render(request, NEW_PAGE, {MEMBER: data, ERROR_MESSAGE:e.message})
    

# def editMember(request, pk):
#     """
#     View function to edit an existing member in the database.
#     On GET request, render the 'edit member' form with the member's current information.
#     On POST request, validate and save the updated member form.
#     """
#     member = Member.objects.get(id=pk)
#     try:
#         if request.method == POST_METHOD:
#             data = member_config.get_data(request.POST)
#             member.first_name=data.get(FIRST_NAME,EMPTY_STRING)
#             member.last_name=data.get(LAST_NAME,EMPTY_STRING)
#             member.email=data.get(EMAIL,EMPTY_STRING)
#             member.phone_number=data.get(PHONE_NUMBER,EMPTY_STRING)
#             member.role=Role(data.get(ROLE,2))
#             member_form = MemberForm(instance=member, data=data)
#             if not member_form.is_valid():
#                 raise TeamManagementFacadeException(member_form.errors.get_json_data())
#             member.save()
#             return redirect(HOME_PAGE)
#         return render(request, EDIT_PAGE, {MEMBER: member})
#     except TeamManagementFacadeException as e:
#         return render(request, EDIT_PAGE, {MEMBER: member, ERROR_MESSAGE:e.message})

# def deleteMember(request, pk):
#     """
#     View function to delete an existing member from the database.
#     On GET request, render the 'delete member' form with the member's information.
#     On POST request, delete the member object from the database.
#     """
#     member = Member.objects.get(id=pk)

#     if request.method == POST_METHOD:
#         member.delete()
#         return redirect(HOME_PAGE)

#     return render(request, DELETE_PAGE, {MEMBER: member})


from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import MemberForm
from .models import Member
from .appConstants import *

class ListMembersView(ListView):
    model = Member
    template_name = 'list.html'
    context_object_name = 'members'
    ordering = 'last_name'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_input = self.request.GET.get('search')
    #     if search_input:
    #         queryset = queryset.filter(first_name__icontains=search_input) | queryset.filter(last_name__icontains=search_input)
    #     return queryset

class AddMemberView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = NEW_PAGE
    success_url = reverse_lazy('list-members')


class EditMemberView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'edit.html'
    success_url = reverse_lazy('list-members')

class DeleteMemberView(DeleteView):
    model = Member
    template_name = 'delete.html'
    success_url = reverse_lazy('list-members')

class MemberDetailView(DetailView):
    model = Member
    template_name = 'list.html'

