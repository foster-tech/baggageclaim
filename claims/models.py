from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from multiselectfield import MultiSelectField

from matches.tasks import calculate_matches
from profiles.tasks import set_available_stamps

booleanChoice = ((True, 'Yes'), (False, 'No'))

class Diets(models.IntegerChoices):
    VEGAN = 0, "Vegan"
    PEWSCATARIAN = 1, "Pescatarian"
    VEGETARIAN = 2, "Vegetarian"
    NON_KOSHER = 3, "Non-kosher"
    KOSHER = 4, "Kosher"
    HALAL = 5, "Halal"
    STRICT = 6, "On a strict diet (Paleo, Keto, Atkins, ect.)"
    MEAT = 7, "A meat eater"

class Pets(models.IntegerChoices):
    DOGS = 0, "Dogs"
    CATS = 1, "Cats"
    BIRDS = 2, "Birds"
    SMALL_MAMMALS = 3, "Small mammals"
    REPTILES = 4, "Reptiles"

class PoliticalViews(models.IntegerChoices):
    CONSERVATIVE = 0, "Conservative"
    LIBERAL = 1, "Liberal"
    MODERATE = 2, "Moderate"

class Religions(models.IntegerChoices):
    CATHOLIC = 0, 'Catholic',
    CHRISTIAN = 1, 'Christian',
    ORTHODOX_JEWISH = 2, 'Orthodox Jewish',
    NON_ORTHODOX_JEWISH = 3, 'Non-Orthodox Jewish',
    BUDDHIST = 4, 'Buddhist',
    MORMON = 5, 'Mormon',
    HINDU = 6, 'Hindu',
    SIKH = 7, 'Sikh',
    ATHEIST = 8, 'Atheist',
    AGNOSTIC = 9, 'Agnostic',
    MUSLIM = 10, 'Muslim',
    OTHER = 11, 'Other',

class Claim1(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='claim1')

    Q1A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q2A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q3A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q4A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q5A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q6A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q7A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q8A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q9A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q10A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q11A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q12A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q13A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q14A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q15A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q16A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q17A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q18A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q19A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q20A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q21A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)

    Q22A = MultiSelectField(choices=Diets.choices, blank=True, null=True, default=None)
    Q23A = models.IntegerField(choices=Diets.choices, blank=True, null=True, default=None)

    Q24A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q25A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)

    Q26A = MultiSelectField(choices=Pets.choices, blank=True, null=True, default=None)
    Q27A = MultiSelectField(choices=PoliticalViews.choices, blank=True, null=True, default=None)
    Q28A = MultiSelectField(choices=Religions.choices, blank=True, null=True, default=None)

class Claim2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='claim2')

    Q29A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q30A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q31A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q32A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q33A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q34A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q35A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q36A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q37A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q38A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q39A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q40A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q41A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q42A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q42B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q43A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q44A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q44B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q45A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q46A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q46B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q47A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q47B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)

class Claim3(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='claim3')

    Q48A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q49A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q50A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q51A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q52A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q53A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q54A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q55A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q56A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q57A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)

class Claim4(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='claim4')

    Q58A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q59A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q60A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q61A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q62A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q63A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q64A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q65A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q66A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q67A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q68A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q69A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q70A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q71A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q72A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q73A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q74A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q75A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q76A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q77A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q78A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q78B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q79A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q79B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q80A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q81A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q81B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q82A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q83A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q84A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q85A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q86A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q86B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q87A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q87B = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q88A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)
    Q89A = models.BooleanField(choices=booleanChoice, blank=False, null=True, default=None)

# TRIGGERS
# Everytime a claim is updated these functions are called
# They are used to update matche scores on the database

@receiver(post_save, sender=Claim1)
def update_user_matches_for_claim1(sender, instance, created, **kwargs):
    if not created:
        calculate_matches.delay(instance.user.id)
        set_available_stamps.delay(instance.user.id, model_to_dict(instance))

@receiver(post_save, sender=Claim2)
def update_user_matches_for_claim2(sender, instance, created, **kwargs):
    if not created:
        calculate_matches.delay(instance.user.id)
        set_available_stamps.delay(instance.user.id, model_to_dict(instance))

@receiver(post_save, sender=Claim3)
def update_user_matches_for_claim3(sender, instance, created, **kwargs):
    if not created:
        calculate_matches.delay(instance.user.id)
        set_available_stamps.delay(instance.user.id, model_to_dict(instance))

@receiver(post_save, sender=Claim4)
def update_user_matches_for_claim4(sender, instance, created, **kwargs):
    if not created:
        calculate_matches.delay(instance.user.id)
        set_available_stamps.delay(instance.user.id, model_to_dict(instance))
