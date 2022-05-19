from django.db import models
from django.conf import settings

class Matches(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_1')
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_2')
	value = models.FloatField(null=False, blank=False, default=-1)
	value_reverse = models.FloatField(null=False, blank=False, default=-1)

	class Meta:
		# Enforce that User1.id must be smaller than User2.id, ensuring that reverse connections are not allowed
		# This might make queries harder since looking up user has to be done on both fields and insertion must be ordered...
		constraints = [
			models.CheckConstraint(
				name='%(class)s_user_id1_lt_id2',
				check = (models.Q(user1__lt = models.F('user2')))
			),
			models.UniqueConstraint(name='%(class)s_user_relation_unique',
				fields=['user1', 'user2'])
		]

	def __str__(self):
		return '{} <> {}'.format(self.user1, self.user2)
