from celery import shared_task
from profiles.models import UserProfile
from matches.question_configs import stamps

@shared_task
def set_available_stamps(uid, claim):
	return do_set_available_stamps(uid, claim)

def do_set_available_stamps(uid, claim):
	profile = UserProfile.objects.get(user=uid)
	if not profile.stamp_count:
		profile.stamp_count = {}

	for k, v in claim.items():
		if k == 'user': continue
		if v: # if yes or some choice from multiple choice
			for stamp in stamps[k]:
				if stamp in profile.stamp_count:
					profile.stamp_count[stamp] += 1
				else:
					profile.stamp_count[stamp] = 1
	profile.save()
