from django.shortcuts import render,redirect
from .forms import RegistrationForm
from battle.models import Player

# Create your views here.
def registration(request):
    if(request.method == 'POST'):
        form = RegistrationForm(data = request.POST)
        if(form.is_valid()):
            user = form.save()
            Player.objects.create(user=user, bot=False)
        return redirect('accounts/login/')
    else:
        form = RegistrationForm()
        return render(request, "registration/reg.html", {'form' : form})
        