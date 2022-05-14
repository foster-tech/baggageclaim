from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from claims.forms import Claim1Form, Claim2Form, Claim3Form, Claim4Form
from claims.models import Claim1, Claim2, Claim3, Claim4
from profiles.models import UserProfile


def redirect_to_correct_claim(filled_claims):
    if filled_claims == 1:
        return redirect('claim2')
    if filled_claims == 2:
        return redirect('claim3')
    if filled_claims == 3:
        return redirect('claim4')
    return redirect('claim1')

@login_required
def ClaimView(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    return redirect_to_correct_claim(user_profile.filled_claims)

@login_required
def Claim1View(request):
    user_profile = UserProfile.objects.get(user=request.user)

    # if this claim doesn't exist in the DB for this user yet we must create it
    claim, created = Claim1.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = Claim1Form(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            user_profile.filled_claims = 1
            user_profile.save()
            return redirect('claim2')
    else:
        # if GET method
        form = Claim1Form(instance=claim)

    # FIXME: temporary workaround to display numbers (form_numbers.Q1A, etc)
    form_numbers = { field[0]: i+1 for i, field in enumerate(form.fields.items()) }

    context = { 'form': form, 'form_numbers': form_numbers }
    return render(request, 'claim1.html', context)

@login_required
def Claim2View(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.filled_claims < 1:
        return redirect_to_correct_claim(user_profile.filled_claims)

    claim, created = Claim2.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = Claim2Form(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            user_profile.filled_claims = 2
            user_profile.save()
            return redirect('claim3')
    else:
        # if GET method
        form = Claim2Form(instance=claim)

    # FIXME: temporary workaround to display numbers (form_numbers.Q1A, etc)
    form_numbers = { field[0]: i+1 for i, field in enumerate(form.fields.items()) }

    context = { 'form': form, 'form_numbers': form_numbers }
    return render(request, 'claim2.html', context)

@login_required
def Claim3View(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.filled_claims < 2:
        return redirect_to_correct_claim(user_profile.filled_claims)

    claim, created = Claim3.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = Claim3Form(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            user_profile.filled_claims = 3
            user_profile.save()
            return redirect('claim4')
    else:
        # if GET method
        form = Claim3Form(instance=claim)

    # FIXME: temporary workaround to display numbers (form_numbers.Q1A, etc)
    form_numbers = { field[0]: i+1 for i, field in enumerate(form.fields.items()) }

    context = { 'form': form, 'form_numbers': form_numbers }
    return render(request, 'claim3.html', context)

@login_required
def Claim4View(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.filled_claims < 3:
        return redirect_to_correct_claim(user_profile.filled_claims)

    claim, created = Claim4.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = Claim4Form(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            user_profile.filled_claims = 4
            user_profile.save()
            return redirect('claim')
    else:
        # if GET method
        form = Claim4Form(instance=claim)

    # FIXME: temporary workaround to display numbers (form_numbers.Q1A, etc)
    form_numbers = { field[0]: i+1 for i, field in enumerate(form.fields.items()) }

    context = { 'form': form, 'form_numbers': form_numbers }
    return render(request, 'claim4.html', context)
