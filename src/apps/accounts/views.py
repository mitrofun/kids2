from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('children:list')
    else:
        form = AuthenticationForm()
    return render_to_response('accounts/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def user_logout(request):
    auth.logout(request)
    return redirect('children:list')
