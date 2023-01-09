import json
from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from django.test import TestCase

from core.models import Member, Role
from . import views

class Testurls(TestCase):

    def test_list_members_url_resolves(self):
        url = reverse("list-members") 
        self.assertEquals(resolve(url).func, views.listMembers)

    def test_add_member_url_resolves(self):
        url = reverse("add-member") 
        self.assertEquals(resolve(url).func, views.addMember)

    def test_edit_member_url_resolves(self):
        url = reverse("edit-member", args=[1]) 
        self.assertEquals(resolve(url).func, views.editMember)

    def test_delete_member_url_resolves(self):
        url = reverse("delete-member", args=[1]) 
        self.assertEquals(resolve(url).func, views.deleteMember)


class ListMembersViewTestCase(TestCase):
    def setUp(self):
        # create some test Member objects
        self.member1 = Member.objects.create(first_name='John', last_name='Doe', email = 'sample1@gmail.com', phone_number = '1234567890')
        self.member2 = Member.objects.create(first_name='Jane', last_name='Doe', email = 'sample2@gmail.com', phone_number = '1234567891')
        self.member3 = Member.objects.create(first_name='Bob', last_name='Smith', email = 'sample3@gmail.com', phone_number = '1234567892')
        
    def test_list_all_members(self):
        response = self.client.get(reverse('list-members'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['members'].count(), 3)
        self.assertEqual(response.context['member_count'], 3)
    
    def test_list_members_by_first_name(self):
        response = self.client.get(reverse('list-members'), {'search-member': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['members'].count(), 1)
        self.assertEqual(response.context['member_count'], 1)
        self.assertEqual(response.context['members'][0], self.member1)
    
    def test_list_members_by_last_name(self):
        response = self.client.get(reverse('list-members'), {'search-member': 'Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['members'].count(), 2)
        self.assertEqual(response.context['member_count'], 2)
        self.assertEqual(response.context['members'][0], self.member1)
        self.assertEqual(response.context['members'][1], self.member2)


class AddMemberViewTestCase(TestCase):
    def setUp(self):

        self.admin = Role.objects.create(role_name='Admin')
        self.regular = Role.objects.create(role_name='Regular')
        
        # create a test form data dictionary
        self.form_data = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com',
            'phoneNumber': '1234567890',
            'role': self.admin.id
        }
        
    def test_add_member(self):
        response = self.client.post(reverse('add-member'), self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Member.objects.count(), 1)
        member = Member.objects.first()
        self.assertEqual(member.first_name, 'John')
        self.assertEqual(member.last_name, 'Doe')
        self.assertEqual(member.email, 'john.doe@example.com')
        self.assertEqual(member.phone_number, '1234567890')
        self.assertEqual(member.role, self.admin)
        
    def test_add_member_with_invalid_form(self):
        # test with missing 'first_name' field
        form_data = self.form_data.copy()
        form_data.pop('firstName')
        response = self.client.post(reverse('add-member'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.count(), 0)
        self.assertEqual(response.context.get('errorMessage'),'first_name field --> This field is required.\n')
        
        # test with invalid 'email' field
        form_data = self.form_data.copy()
        form_data['email'] = 'invalid_email'
        response = self.client.post(reverse('add-member'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.count(), 0)
        self.assertEqual(response.context.get('errorMessage'),'email field --> Enter a valid email address.\n')
        



class EditMemberViewTestCase(TestCase):
    def setUp(self):
        # create some test Role objects
        self.admin = Role.objects.create(role_name='Admin')
        self.regular = Role.objects.create(role_name='Regular')
        
        # create a test Member object
        self.member = Member.objects.create(
            first_name='John', last_name='Doe', email='john.doe@example.com',
            phone_number='1234567890', role=self.admin
        )
        
        # create a test form data dictionary
        self.form_data = {
            'firstName': 'Jane',
            'lastName': 'Doe',
            'email': 'jane.doe@example.com',
            'phoneNumber': '1234567891',
            'role': self.regular.id
        }
        
    def test_edit_member(self):
        response = self.client.post(reverse('edit-member', kwargs={'pk': self.member.id}), self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Member.objects.count(), 1)
        member = Member.objects.first()
        self.assertEqual(member.first_name, 'Jane')
        self.assertEqual(member.last_name, 'Doe')
        self.assertEqual(member.email, 'jane.doe@example.com')
        self.assertEqual(member.phone_number, '1234567891')
        self.assertEqual(member.role, self.regular)
        
    def test_edit_member_with_invalid_form(self):
        # test with missing 'first_name' field
        form_data = self.form_data.copy()
        form_data.pop('firstName')
        response = self.client.post(reverse('edit-member', kwargs={'pk': self.member.id}), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.count(), 1)
        self.assertEqual(response.context.get('errorMessage'),'first_name field --> This field is required.\n')
        
        # test with invalid 'email' field
        form_data = self.form_data.copy()
        form_data['email'] = 'invalid_email'
        response = self.client.post(reverse('edit-member', kwargs={'pk': self.member.id}), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.count(), 1)
        self.assertEqual(response.context.get('errorMessage'),'email field --> Enter a valid email address.\n')
 
