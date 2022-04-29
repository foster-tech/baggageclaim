from pydoc import locate

import numpy as np
from celery import shared_task
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from matches.models import Matches
from matches.question_configs import relationships
from profiles.models import UserProfile

@shared_task
def calculate_matches(uid):
    return do_calculate_matches(uid)

# separate this function to allow it to run it in tests without celery
def do_calculate_matches(uid):
    user = User.objects.get(pk=uid)
    profile = UserProfile.objects.get(user=user)

    # get all filled data
    claim_list = get_list_claims(user, profile.filled_claims)
    updated_matches = 0

    for other in User.objects.all():
        if other.is_superuser or other.is_staff or user.id == other.id: continue

        # get the other user data
        other_filled_claims = UserProfile.objects.get(user=other).filled_claims
        other_claim_data = merge_claim_list(get_list_claims(other, min(profile.filled_claims, other_filled_claims)))
        if not other_claim_data: continue

        claim_data = merge_claim_list(claim_list, min(profile.filled_claims, other_filled_claims))

        r_user_other = calc(claim_data, other_claim_data, relationships)
        r_other_user = calc(other_claim_data, claim_data, relationships)

        # set users and results in correct order (u1.id < u2.id) to insert in the database
        u1, u2, r1, r2 = (user, other, r_user_other, r_other_user) if user.id < other.id else (other, user, r_other_user, r_user_other)

        try:
            m = Matches.objects.get(user1=u1, user2=u2)
        except Matches.DoesNotExist:
            Matches.objects.create(user1=u1, user2=u2, value=r1, value_reverse=r2)
            updated_matches += 1
        else:
            m.value, m.value_reverse = r1, r2
            m.save()
            updated_matches += 1
    return updated_matches

def get_list_claims(user, filled_claims):
    '''Get claims data from DB and return a list of dictionaries with each claim'''
    claim_data = []
    for i in range(filled_claims):
        Claim = locate(f'claims.models.Claim{i+1}') # TODO Take this out of here (needed beacause claims.models also imports this module)
        claim_data.append(model_to_dict(Claim.objects.get(user=user)))
    return claim_data

def merge_claim_list(claim_data, filled_claims=4):
    r = {}
    for d in claim_data[:min(filled_claims, len(claim_data))]: r.update(d)
    return r

# Algorithm functions

def calc(p1, p2, relationships):

    sum=0
    for question, answer in p1.items():
        if question in relationships:
            for relation, func in relationships[question].items():
                if relation in p2:
                    x=func(answer, p2[relation])
                    if x==9999:
                        return x
                    else:
                        sum+=x
    return sum

