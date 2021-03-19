import ipaddress

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseServerError
from django.urls import reverse_lazy
from django.views import generic



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'





def byId(request,id):
    users = User.objects.all()
    for user in users:
        up_user=User.objects.get(username=user)
        up_id=up_user.id
        if id == up_id:
            profile = {
                'Id' : up_id,
                'Username' : up_user.username,
                'Registration Date' : up_user.date_joined,
            }
            return JsonResponse(profile)
    return HttpResponseServerError("No users for this ID")
