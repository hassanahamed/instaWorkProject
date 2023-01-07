from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .team_management_exception import TeamManagementFacadeException
from .forms import MemberForm
from .models import Member, Role
from .mapper_config import MemberConfig
from .appConstants import *


# Create your views here.
member_config = MemberConfig()
def index(request):
    members = Member.objects.all()
    search_input = request.GET.get(SEARCH)
    if search_input:
        first_name_members = Member.objects.filter(first_name__icontains=search_input)
        last_name_members = Member.objects.filter(last_name__icontains=search_input)
        members = (first_name_members | last_name_members).distinct()
    else:
        members = Member.objects.all()
        search_input = EMPTY_STRING
    return render(request, INDEX_PAGE, {MEMBERS: members, SEARCH: search_input, MEMBER_COUNT: len(members)})

def addMember(request):
    
    data = member_config.get_data(request.POST)
    new_member_form = MemberForm(data)
    try:
        if request.method == POST_METHOD:
            if not new_member_form.is_valid():
                raise TeamManagementFacadeException(new_member_form.errors.get_json_data())
            new_member = new_member_form.save(commit=False)
            new_member.role = Role(request.POST.get(ROLE,DEFAULT_ROLE))
            new_member.save()
            return redirect(HOME_PAGE)

        return render(request, NEW_PAGE, {MEMBER: EMPTY_STRING})
    except TeamManagementFacadeException as e:
        return render(request, NEW_PAGE, {MEMBER: data, ERROR_MESSAGE:e.message})


            

def editMember(request, pk):
    member = Member.objects.get(id=pk)
    try:
        if request.method == POST_METHOD:
            data = member_config.get_data(request.POST)
            member.first_name=data.get(FIRST_NAME,EMPTY_STRING)
            member.last_name=data.get(LAST_NAME,EMPTY_STRING)
            member.email=data.get(EMAIL,EMPTY_STRING)
            member.phone_number=data.get(PHONE_NUMBER,EMPTY_STRING)
            member.role=Role(data.get(ROLE,2))
            member_form = MemberForm(instance=member, data=data)
            if not member_form.is_valid():
                raise TeamManagementFacadeException(member_form.errors.get_json_data())
            member.save()
            return redirect(HOME_PAGE)
        return render(request, EDIT_PAGE, {MEMBER: member})
    except TeamManagementFacadeException as e:
        return render(request, EDIT_PAGE, {MEMBER: member, ERROR_MESSAGE:e.message})

def deleteMember(request, pk):
    member = Member.objects.get(id=pk)

    if request.method == POST_METHOD:
        member.delete()
        return redirect(HOME_PAGE)

    return render(request, DELETE_PAGE, {MEMBER: member})
