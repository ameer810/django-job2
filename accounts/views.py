from django.shortcuts import redirect, render, reverse
from .forms import SignupForms, ProfileForm, UserForm,iam
from django.contrib.auth import authenticate, login
from .models import Profile,City


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForms()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile': profile})


def profile_edit(request):
    contry= City.objects.all()
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userforme = UserForm(request.POST, instance=request.user)
        contryforme = iam(request.POST, instance=request.user)
        profileforme = ProfileForm(request.POST, request.FILES, instance=profile)
        if userforme.is_valid() and profileforme.is_valid():
            userforme.save()
            myprofile = profileforme.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userforme = UserForm(instance=request.user)
        profileforme = ProfileForm(instance=profile)
        contryforme = iam()

    return render(request, 'account/profile_edit.html', {'userform': userforme, 'profileform': profileforme,'contryforme':contryforme})


def cont(request):
    contry= City.objects.all()
    return render(request, 'account/profile_edit.html', {'contry': contry})