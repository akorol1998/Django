from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class RegisterView(generic.FormView):
    form = UserCreationForm()
    
    def post(self, request):
        return render(request )


    def get(self, request):
        return render(request, 'users/register.html', {"form":self.form})