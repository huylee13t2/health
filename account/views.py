from time import time

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect
from django.urls.base import reverse
from account import permission
from account.forms import RegisterForm


def choose_profile(request):
    user_account_type = request.user.cwghmouser.account_type
    if user_account_type == 'Private Customer':
        ''' redirect to private customer profile/complete signup page if need be '''
        return redirect(reverse('frontend:homepage')) # for now redirect home
    elif user_account_type == 'Corporate Customer':
        return redirect(reverse('frontend:homepage'))  # for now redirect home
    elif user_account_type == 'Provider':
        return redirect(reverse('frontend:homepage'))  # for now redirect home
    elif user_account_type == 'HMO':
        return redirect(reverse('frontend:homepage'))  # for now redirect home
    else:
        return redirect(reverse('frontend:homepage'))  # for now redirect home


def user_registration(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cwqhmo_user = form.save()
            ''' Now adding user to the permission group and roles'''
            assign_user_permission(cwqhmo_user.user)
            ''' Email verification process might come intto play if need be'''
            user = authenticate(username=cwqhmo_user.user.email, password=request.POST['password'])
            if (user and user.is_active):
                login(request, user)
                messages.success(request, 'Your registration was successful')
            return redirect(reverse('account:choose_profile'))
    context ={
        'form':form
    }
    return render(request,'account/signup.html', context)


def assign_user_permission(user):
    if user.cwghmouser.account_type == 'Private Customer':
        user.user_permissions.add(Permission.objects.get(codename='private_customer'))
    elif user.cwghmouser.account_type == 'Corporate Customer':
        user.user_permissions.add(Permission.objects.get(codename='corporate_customer'))
    elif user.cwghmouser.account_type == 'Provider':
        user.user_permissions.add(Permission.objects.get(codename='provider'))
    elif user.cwghmouser.account_type == 'HMO':
        user.user_permissions.add(Permission.objects.get(codename='hmo'))
    user.save()
    return True