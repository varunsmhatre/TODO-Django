from django.shortcuts import render, redirect
from .forms import UserRegisterForm, RequestPasswordResetForm
from django.contrib import messages


# Create your views here.
# @login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def request_password_reset(request):
    if request.method == 'POST':
        form = RequestPasswordResetForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # send_password_reset_mail()
            messages.success(request, f'Password Reset Mail Sent! Please reset your password in 15 mins!')
            return redirect('about')
    else:
        form = RequestPasswordResetForm()
    return render(request, 'users/request_password_reset.html', {'form':form})
