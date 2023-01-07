from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .team_management_exception import TeamManagementFacadeException
from .forms import MemberForm
from .models import Member, Role
from .mapper_config import MemberConfig


# Create your views here.
member_config = MemberConfig()
def index(request):
    members = Member.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        first_name_members = Member.objects.filter(first_name__icontains=search_input)
        last_name_members = Member.objects.filter(last_name__icontains=search_input)
        members = (first_name_members | last_name_members).distinct()
    else:
        members = Member.objects.all()
        search_input = ''
    return render(request, 'index.html', {'members': members, 'search_input': search_input, 'member_count': len(members)})

def addMember(request):
    
    data = member_config.get_data(request.POST)
    print(data)
    new_member_form = MemberForm(data)
    try:
        if request.method == 'POST':
            if not new_member_form.is_valid():
                raise TeamManagementFacadeException(new_member_form.errors.get_json_data())
            
            new_member = new_member_form.save(commit=False)
            new_member.role = Role(request.POST.get("role",2))
            new_member.save()
            return redirect('/')

        return render(request, 'new.html', {'member': ''})
    except TeamManagementFacadeException as e:
        return render(request, 'new.html', {'member': data, 'errorMessage':e.message})


            

def editMember(request, pk):
    member = Member.objects.get(id=pk)
    try:
        if request.method == 'POST':
            data = member_config.get_data(request.POST)
            member.first_name=request.POST['firstName']
            member.last_name=request.POST['lastName']
            member.email=request.POST['email']
            member.phone_number=request.POST['phoneNumber']
            member.role=Role(request.POST.get("role",2))
            member_form = MemberForm(instance=member, data=data)
            if not member_form.is_valid():
                raise TeamManagementFacadeException(member_form.errors.get_json_data())
            member.save()
            return redirect('/')
        return render(request, 'edit.html', {'member': member})
    except TeamManagementFacadeException as e:
        return render(request, 'edit.html', {'member': member, 'errorMessage':e.message})

def deleteMember(request, pk):
    member = Member.objects.get(id=pk)

    if request.method == 'POST':
        member.delete()
        return redirect('/')

    return render(request, 'delete.html', {'member': member})
