from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import render

from matches.models import Matches
from profiles.models import UserProfile, Genders, SexualOrientations, EducationLevels, Religions, Children, Destinations, Stamps

@login_required
def DestinationView(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.filled_claims < 1:
        pass # TODO SHOW SOME MESSAGE

    matches = []
    db_matches = Matches.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    for m in db_matches:
        other_profile = UserProfile.objects.get(user=m.user1) if m.user1 != request.user else UserProfile.objects.get(user=m.user2)
        fc = min(user_profile.filled_claims, other_profile.filled_claims)
        stamps = [Stamps.labels[int(s)] for s in other_profile.selected_stamps]
        matches.append(
            {'user': other_profile, 'match': get_match_level(m.value, fc), 'stamps': stamps}
                if m.user1 != request.user
                else {'user': other_profile, 'match': get_match_level(m.value_reverse, fc), 'stamps': stamps})

    context = {'matches': matches }

    return render(request, 'destination.html', context)

def get_match_level(score, filled_claims):
    if filled_claims == 1:
        if score > 17.5: return 5 # Crash & Burn
        elif score > 13: return 4 # Low match
        elif score > 8.5: return 3 # Medium match
        elif score > 4: return 2 # High match
        else: return 1 # Cloud 9
    elif filled_claims == 2:
        if score > 31.5: return 5 # Crash & Burn
        elif score > 24: return 4 # Low match
        elif score > 16: return 3 # Medium match
        elif score > 8: return 2 # High match
        else: return 1 # Cloud 9
    elif filled_claims == 3:
        if score > 37.5: return 5 # Crash & Burn
        elif score > 28: return 4 # Low match
        elif score > 18: return 3 # Medium match
        elif score > 9: return 2 # High match
        else: return 1 # Cloud 9
    elif filled_claims == 4:
        if score > 59.5: return 5 # Crash & Burn
        elif score > 44.5: return 4 # Low match
        elif score > 29.5: return 3 # Medium match
        elif score > 14.5: return 2 # High match
        else: return 1# Cloud 9
