from itertools import chain
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from .models import Member
from django.core.validators import validate_email

# Create your views here.

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
    new_member = None
    try:
        if request.method == 'POST':
            
            new_member = Member(
                first_name=request.POST['firstName'],
                last_name=request.POST['lastName'],
                email=request.POST['email'],
                phone_number=request.POST['phoneNumber'],
                is_admin=request.POST['isAdmin'],
                )
            validate_email(request.POST['email'])
            new_member.save()
            return redirect('/')

        return render(request, 'new.html')
    except ValidationError as e:
        e = list(e)
        print(e[0])
        return render(request, 'new.html', {'member': new_member, 'errorMessage':e[0]})

    except IntegrityError as e:
        print(e)
        e = str(e)
        error_message = e
        if 'core_member.email' in e:
            error_message = 'Email Address already exists'
        if 'core_member.phone_number' in e:
            error_message = 'Phone number already exists'
        return render(request, 'new.html', {'member': new_member, 'errorMessage':error_message})

            

def editMember(request, pk):
    member = Member.objects.get(id=pk)
    try:
        if request.method == 'POST':
            print(request.POST['isAdmin'])
            member.first_name=request.POST['firstName']
            member.last_name=request.POST['lastName']
            member.email=request.POST['email']
            member.phone_number=request.POST['phoneNumber']
            member.is_admin=request.POST['isAdmin']
            validate_email(request.POST['email'])
            member.save()

            return redirect('/')
        return render(request, 'edit.html', {'member': member})
    except ValidationError as e:
        e = list(e)
        print(e[0])
        return render(request, 'edit.html', {'member': member, 'errorMessage':e[0]})

    except IntegrityError as e:
        print(e)
        e = str(e)
        error_message = e
        if 'core_member.email' in e:
            error_message = 'Email Address already exists'
        if 'core_member.phone_number' in e:
            error_message = 'Phone number already exists'
        return render(request, 'edit.html', {'member': member, 'errorMessage':error_message})

def deleteMember(request, pk):
    member = Member.objects.get(id=pk)

    if request.method == 'POST':
        member.delete()
        return redirect('/')

    return render(request, 'delete.html', {'member': member})
