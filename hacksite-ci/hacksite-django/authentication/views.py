import logging
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as _login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
# from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm, User, ChangePasswordForm


logger = logging.getLogger(__name__)


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.data["username"]
            password = form.data["password"]
            User.objects.create_user(username, '', password)
            return HttpResponseRedirect(reverse('login'))
        else:
            logger.info(form.errors)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    context = {}
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            _login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = UserForm(request.POST)
            context['message'] = 'Wrong username or password'
    else:
        form = UserForm()
    context['form'] = form
    return render(request, 'authentication/login.html', context)


@login_required
def change_password(request, pk=None):
    user = User.objects.get(pk=pk) if pk else request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.data["password"]
            user.set_password(password)
            user.save()
            return logout_then_login(request)
        else:
            logger.info(form.errors)
    else:
        form = ChangePasswordForm()
    context = {'form': form, 'user': user}
    return render(request, 'authentication/change-password.html', context)
