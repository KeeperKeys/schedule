from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required


def login(request):
    errors = {}
    if request.user.is_authenticated():
        # return HttpResponseRedirect("/accounts/loggedout/")
        errors['authorization'] = True
        return render_to_response('users/login.html', errors, context_instance=RequestContext(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/accounts/loggedin/")
        else:
            return HttpResponseRedirect("/accounts/login/?q=login_error")
    if 'q' in request.GET:
        q = request.GET['q']
        if q == 'login_error':
            errors['login_error'] = True
    return render_to_response('users/login.html', errors, context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/loggedout/?q=loqout")


@login_required
def loggedin(request):
    return render_to_response('users/loggedin.html', context_instance=RequestContext(request))


def loggedout(request):
    if 'q' in request.GET and not request.user.is_authenticated():
        q = request.GET['q']
        if q == 'loqout':
            return render_to_response(r'users/loggedout.html', {'userlogout': True},
                                      context_instance=RequestContext(request))
    if not request.user.is_authenticated():
        return render_to_response(r'users/loggedout.html', context_instance=RequestContext(request))
    return render_to_response(r'users/loggedout.html', {'uservalid': True, 'user': request.user},
                              context_instance=RequestContext(request))
