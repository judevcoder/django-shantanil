from django.views.generic import TemplateView
from django.http import *
from django.db import models
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import UserLogger
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


@login_required(login_url='/accounts/login/')
def home(request):
    return HttpResponseRedirect('/dashboard/')

class LimitExceeed(PermissionDenied):
    pass

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # user_ip = get_user_ip(request)
            # user_hostname = socket.gethostbyaddr(user_ip)[0]
            if User.objects.count() > 4:
                raise LimitExceeed
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            created_user = User.objects.get(id=user.id)

            logger = UserLogger(
                login_ipaddress=get_user_ip(request),
                login_hostname=request.META['HTTP_HOST'],
                username=username,
                user=created_user
            )

            logger.save()

            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        next_page = None
        try:
            next_page = request.POST['next']
        except:
            pass

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                created_user = User.objects.get(id=user.id)

                logger = UserLogger(
                    login_ipaddress=get_user_ip(request),
                    login_hostname=request.META['HTTP_HOST'],
                    username=username,
                    user=created_user
                )

                logger.save()

                if next_page:
                    return HttpResponseRedirect(next_page, {'user': user})
                return HttpResponseRedirect('/dashboard/', {'user':user})
    return HttpResponseRedirect('/accounts/login')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    user = request.user
    users = User.objects.all().order_by('id')
    return render_to_response('pages/dashboard.html', locals(), RequestContext(request))


@login_required(login_url='/accounts/login/')
def connection_adapter(request):
    return render_to_response('pages/connection_adapter.html')


@login_required(login_url='/accounts/login/')
def connection(request):
    user = request.user
    users = User.objects.all().order_by('id')
    return render_to_response('pages/connection.html', locals(), RequestContext(request))


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# def adapter(request):
