from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import redirect, render

from profiles.forms import RegisterForm, UserProfileForm, Stamps
from profiles.models import ProfilePhoto, UserProfile

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def ProfileView(request):
    # get user profile
    user_profile = UserProfile.objects.get(user=request.user)
    form = None

    if request.method == 'POST':
        # load form data
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            if 'profile_photos' in form.changed_data:   # FIXME: improve this verification to not delete/save every time
                user_profile.profile_photos.all().delete() # clean up before save it all
                for image in request.FILES.getlist('profile_photos'):
                    ProfilePhoto.objects.create(image=image, user=user_profile)
            user.save()
            try:
                form.save()
                return redirect('mypassport')
            except IntegrityError as e: # Most likely this is due to the age restriction...
                print(f'\033[1;31m{e}\033[m')
    elif request.method == 'GET':
        # create form with data from the database
        form = UserProfileForm(instance=user_profile)

    # make data accessible to the html template
    context = {
        'user_profile': user_profile,
        'profile_photos': list(user_profile.profile_photos.all()),
        'form': form,
    }
    return render(request, 'profile.html', context)

@login_required
def PassportView(request):
    # get user profile
    user_profile = UserProfile.objects.get(user=request.user)
    form = None

    if request.method == 'GET':
        # create form with data from the database
        form = UserProfileForm(instance=user_profile)

    # make data accessible to the html template
    context = {
        'user_profile': user_profile,
        'stamps': [Stamps.labels[int(s)] for s in user_profile.selected_stamps],
        'form': form,
    }
    return render(request, 'mypassport.html', context)
