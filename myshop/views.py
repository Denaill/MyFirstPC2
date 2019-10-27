from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)