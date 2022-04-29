# vi: foldmethod=marker
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from jsonfield import JSONField
from multiselectfield import MultiSelectField


# CHOICE CLASSES {{{
class Genders(models.IntegerChoices):
    MALE = 0, 'Male',
    FEMALE = 1, 'Female',
    NON_BINARY = 2, 'Non-binary',
    FEMALE_TRANSGENDER = 3, 'Female Transgender',
    MALE_TRANSGENDER = 4, 'Male Transgender',

class SexualOrientations(models.IntegerChoices):
    STRAIGHT = 0, 'Straight',
    GAY = 1, 'Gay',
    LESBIAN = 2, 'Lesbian',
    BISEXUAL = 3, 'Bisexual',
    PANSEXUAL = 4, 'Pansexual',
    QUEER = 5, 'Queer',

class EducationLevels(models.IntegerChoices):
    HIGHT_SCHOOL = 0, 'High School',
    TRADE_SCHOOL = 1, 'Trade School',
    SOME_COLLEGE = 2, 'Some College',
    UNDERGRADUATE_DEGREE = 3, 'Undergraduate Degree',
    GRADUATE_DEGREE = 4, 'Graduate Degree',

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

class Children(models.IntegerChoices):
    NO_CHILDREN = 0, 'No children',
    SMALL_CHILDREN = 1, 'Small children',
    PRE_TEEN_TEEN_CHILDREN = 2, 'Pre-teen/Teen children',
    ADULT_CHILDREN = 3, 'Adult children',

class Destinations(models.IntegerChoices):
    RELATIONSHIP = 0, 'Relationship',
    SOMETHING_CASUAL = 1, 'Something casual',
    IDK_YET = 2, 'I don’t know yet',
    MARRIAGE = 3, 'Marriage',

class Stamps(models.IntegerChoices):
    NONE             = 0, 'None',
    ABANDONMENT      = 1, 'Abandonment',
    AVOIDANT         = 2, 'Avoidant',
    WORKAHOLIC       = 3, 'Workaholic',
    DRAMATIC         = 4, 'Dramatic',
    CHEAPSKATE       = 5, 'Cheapskate',
    HYPERSENSITIVE   = 6, 'Hypersensitive',
    CIGARETTESMOKER  = 7, 'Cigarette Smoker',
    OVERWHELMED      = 8, 'Overwhelmed',
    UNREFINED        = 9, 'Unrefined',
    LONER            = 10, 'Loner',
    STAGNANT         = 11, 'Stagnant',
    NEGATIVENAT      = 12, 'Negativenat',
    PERFECTIONIST    = 13, 'Perfectionist',
    UNRELIABLE       = 14, 'Unreliable',
    WILDCARD         = 15, 'Wildcard',
    NOBOUNDARIES     = 16, 'Noboundaries',
    SELFCENTERED     = 17, 'Selfcentered',
    POORCOMMUNICATOR = 18, 'Poor Communicator',
    TRUSTISSUES      = 19, 'Trust Issues',
    RESENTFUL        = 20, 'Resentful',

# }}}

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='profile')

    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)

    age = models.IntegerField(blank=True, null=True)

    user_avatar = models.ImageField(upload_to="media/", blank=True, null=True)

    location_city = models.CharField(max_length=30, blank=True, null=True)
    location_state = models.CharField(max_length=30, blank=True, null=True)
    location_country = models.CharField(max_length=30, blank=True, null=True)

    gender = models.IntegerField(
        choices=Genders.choices,
        blank=True,
        null=True)
    sexual_orientation = models.IntegerField(
        choices=SexualOrientations.choices,
        blank=True,
        null=True)
    education = models.IntegerField(
        choices=EducationLevels.choices,
        blank=True,
        null=True)

    religion = MultiSelectField(
        choices=Religions.choices,
        blank=True,
        null=True)
    children = MultiSelectField(
        choices=Children.choices,
        blank=True,
        null=True)
    destination = MultiSelectField(
        choices=Destinations.choices,
        blank=True,
        null=True)

    question1 = models.CharField(max_length=300, blank=True, null=True)
    question2 = models.CharField(max_length=300, blank=True, null=True)
    question3 = models.CharField(max_length=300, blank=True, null=True)
    question4 = models.CharField(max_length=300, blank=True, null=True)
    question5 = models.CharField(max_length=300, blank=True, null=True)
    question6 = models.CharField(max_length=300, blank=True, null=True)

    # dictionary with count of available stamps
    stamp_count = JSONField(blank=True, null=True)
    selected_stamps = MultiSelectField(choices=Stamps.choices, max_choices=2, blank=True, null=True)

    filled_claims = models.IntegerField(null=False, default=0)

    class Meta:
        # Enforce that User1.id must be smaller than User2.id, ensuring that reverse connections are not allowed
        # This might make queries harder since looking up user has to be done on both fields and insertion must be ordered...
        constraints = [
            models.CheckConstraint(
                name='%(class)s_age_gt_18',
                check = (models.Q(age__gte = 18))
            )
        ]

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
