from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def account(request):
    return render(request, 'account/account.html')

def edit_user(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        form = UserForm(instance=user)
        return render(request, 'account/account_form.html', {'form': form})
    else:
        user = User.objects.get(id=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('account')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('account')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})