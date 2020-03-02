from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegisterView(generic.FormView):
    form = UserRegisterForm()
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created for {username}")
            return redirect('login')
        else:
            return render(request, 'users/register.html', {"form":form})


    def get(self, request):
        return render(request, 'users/register.html', {"form":self.form})

class ProfileView(LoginRequiredMixin, generic.View):
    login_url = 'login'
    # redirect_field_name = 'blog-home'
    
    def get(self, request):
        return render(request, "users/profile.html")