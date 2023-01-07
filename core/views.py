from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .team_management_exception import TeamManagementFacadeException
from .forms import MemberForm
from .models import Member, Role
from .mapper_config import MemberConfig
from .appConstants import *

# Create an instance of the MemberConfig class to use for mapping data
member_config = MemberConfig()

def index(request):
    """
    View function to display a list of all members, with the option to search for members by name.
    If a search query is provided, return a list of members whose first or last name match the search query.
    Otherwise, return a list of all members.
    """
    members = Member.objects.all()
    search_input = request.GET.get(SEARCH)
    if search_input:
        first_name_members = Member.objects.filter(first_name__icontains=search_input)
        last_name_members = Member.objects.filter(last_name__icontains=search_input)
        # Combine the two querysets and remove any duplicate members
        members = (first_name_members | last_name_members).distinct()
    else:
        members = Member.objects.all()
        search_input = EMPTY_STRING
    return render(request, INDEX_PAGE, {MEMBERS: members, SEARCH: search_input, MEMBER_COUNT: len(members)})

def addMember(request):
    """
    View function to add a new member to the database.
    On GET request, render the 'new member' form.
    On POST request, validate and save the new member form.
    """
    # Map the POST data to the expected keys specified in the member_config object
    data = member_config.get_data(request.POST)
    new_member_form = MemberForm(data)
    try:
        if request.method == POST_METHOD:
            if not new_member_form.is_valid():
                # If the form is invalid, raise an exception with the form errors as the message
                raise TeamManagementFacadeException(new_member_form.errors.get_json_data())
            new_member = new_member_form.save(commit=False)
            new_member.role = Role(request.POST.get(ROLE,DEFAULT_ROLE))
            new_member.save()
            return redirect(HOME_PAGE)

        return render(request, NEW_PAGE, {MEMBER: EMPTY_STRING})
    except TeamManagementFacadeException as e:
        return render(request, NEW_PAGE, {MEMBER: data, ERROR_MESSAGE:e.message})
    

def editMember(request, pk):
    """
    View function to edit an existing member in the database.
    On GET request, render the 'edit member' form with the member's current information.
    On POST request, validate and save the updated member form.
    """
    # Retrieve the member object to be edited
    member = Member.objects.get(id=pk)
    try:
        if request.method == POST_METHOD:
            # Map the POST data to the expected keys specified in the member_config object
            data = member_config.get_data(request.POST)
            # Update the member object's attributes with the mapped data
            member.first_name=data.get(FIRST_NAME,EMPTY_STRING)
            member.last_name=data.get(LAST_NAME,EMPTY_STRING)
            member.email=data.get(EMAIL,EMPTY_STRING)
            member.phone_number=data.get(PHONE_NUMBER,EMPTY_STRING)
            member.role=Role(data.get(ROLE,2))
            # Create a form instance with the updated member object and the mapped data
            member_form = MemberForm(instance=member, data=data)
            if not member_form.is_valid():
                # If the form is invalid, raise an exception with the form errors as the message
                raise TeamManagementFacadeException(member_form.errors.get_json_data())
            member.save()
            return redirect(HOME_PAGE)
        return render(request, EDIT_PAGE, {MEMBER: member})
    except TeamManagementFacadeException as e:
        return render(request, EDIT_PAGE, {MEMBER: member, ERROR_MESSAGE:e.message})

def deleteMember(request, pk):
    """
    View function to delete an existing member from the database.
    On GET request, render the 'delete member' form with the member's information.
    On POST request, delete the member object from the database.
    """
    # Retrieve the member object to be deleted
    member = Member.objects.get(id=pk)

    if request.method == POST_METHOD:
        member.delete()
        return redirect(HOME_PAGE)

    return render(request, DELETE_PAGE, {MEMBER: member})
