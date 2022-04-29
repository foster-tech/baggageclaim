from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import TestCase

from claims.models import Claim1, Claim2, Claim3, Claim4
from matches.models import Matches
from profiles.tasks import do_set_available_stamps
from profiles.models import UserProfile

class ProfileStampsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='12345')
        c = Claim1.objects.create(user=self.user1,
            Q1A = False, Q2A = True, Q3A = False, Q4A = True, Q5A = True, Q6A = False,
            Q7A = True, Q8A = False, Q9A = True, Q10A = False, Q11A = False, Q12A = False,
            Q13A = True, Q14A = True, Q15A = False, Q16A = False, Q17A = False, Q18A = True,
            Q19A = True, Q20A = True, Q21A = False, Q22A = ['0', '2', '3'], Q23A = 2,
            Q24A = False, Q25A = False, Q26A = ['3', '4'], Q27A = ['0'], Q28A = ['4','5','6','7','9','10']
        )
        do_set_available_stamps(self.user1.id, model_to_dict(c))
        c = Claim2.objects.create(user=self.user1,
            Q29A = False, Q30A = True, Q31A = True, Q32A = False, Q33A = True, Q34A = False,
            Q35A = False, Q36A = False, Q37A = True, Q38A = True, Q39A = True, Q40A = False,
            Q41A = True, Q42A = False, Q42B = True, Q43A = True, Q44A = True, Q44B = False,
            Q45A = False, Q46A = False, Q46B = True, Q47A = True, Q47B = False
        )
        do_set_available_stamps(self.user1.id, model_to_dict(c))
        c = Claim3.objects.create(user=self.user1,
            Q48A = False, Q49A = True, Q50A = False, Q51A = True, Q52A = True, Q53A = False,
            Q54A = True, Q55A = True, Q56A = True, Q57A = True
        )
        do_set_available_stamps(self.user1.id, model_to_dict(c))
        c = Claim4.objects.create(user=self.user1,
            Q58A = False, Q59A = True, Q60A = False, Q61A = True, Q62A = True, Q63A = True,
            Q64A = False, Q65A = False, Q66A = False, Q67A = True, Q68A = True, Q69A = False,
            Q70A = True, Q71A = False, Q72A = True, Q73A = True, Q74A = True, Q75A = False,
            Q76A = False, Q77A = False, Q78A = True, Q78B = True, Q79A = False, Q79B = False,
            Q80A = True, Q81A = True, Q81B = True, Q82A = False, Q83A = False, Q84A = True,
            Q85A = True, Q86A = False, Q86B = True, Q87A = True, Q87B = False, Q88A = True,
            Q89A = False
        )
        do_set_available_stamps(self.user1.id, model_to_dict(c))
        profile = UserProfile.objects.get(user=self.user1)
        profile.filled_claims = 4
        profile.save()

        self.user2 = User.objects.create_user(username='user2', password='12345')
        c = Claim1.objects.create(user=self.user2,
            Q1A = False, Q2A = False, Q3A = True, Q4A = False, Q5A = False, Q6A = False,
            Q7A = True, Q8A = False, Q9A = True, Q10A = False, Q11A = False, Q12A = True,
            Q13A = False, Q14A = True, Q15A = False, Q16A = False, Q17A = False, Q18A = True,
            Q19A = True, Q20A = False, Q21A = False, Q22A = ['0', '2', '3'], Q23A = 2,
            Q24A = False, Q25A = False, Q26A = ['3', '4'], Q27A = ['0'], Q28A = ['4','5','6','7','9','10']
        )
        do_set_available_stamps(self.user2.id, model_to_dict(c))
        c = Claim2.objects.create(user=self.user2,
            Q29A = True, Q30A = False, Q31A = False, Q32A = False, Q33A = False, Q34A = True,
            Q35A = True, Q36A = False, Q37A = False, Q38A = True, Q39A = True, Q40A = False,
            Q41A = True, Q42A = True, Q42B = False, Q43A = True, Q44A = True, Q44B = False,
            Q45A = False, Q46A = False, Q46B = True, Q47A = False, Q47B = False
        )
        do_set_available_stamps(self.user2.id, model_to_dict(c))
        profile = UserProfile.objects.get(user=self.user2)
        profile.filled_claims = 2
        profile.save()

        self.user3 = User.objects.create_user(username='user3', password='12345')
        c = Claim1.objects.create(user=self.user3,
            Q1A = False, Q2A = True, Q3A = False, Q4A = False, Q5A = True, Q6A = True,
            Q7A = True, Q8A = False, Q9A = False, Q10A = False, Q11A = False, Q12A = False,
            Q13A = True, Q14A = True, Q15A = False, Q16A = False, Q17A = False, Q18A = True,
            Q19A = True, Q20A = False, Q21A = False, Q22A = ['0', '2', '3'], Q23A = 3,
            Q24A = False, Q25A = True, Q26A = ['3', '4'], Q27A = ['0'], Q28A = ['4','5','6','7','9','10']
        )
        do_set_available_stamps(self.user3.id, model_to_dict(c))
        c = Claim2.objects.create(user=self.user3,
            Q29A = False, Q30A = False, Q31A = True, Q32A = False, Q33A = True, Q34A = False,
            Q35A = False, Q36A = True, Q37A = False, Q38A = False, Q39A = True, Q40A = False,
            Q41A = True, Q42A = False, Q42B = True, Q43A = False, Q44A = True, Q44B = False,
            Q45A = True, Q46A = False, Q46B = False, Q47A = True, Q47B = False
        )
        do_set_available_stamps(self.user3.id, model_to_dict(c))
        c = Claim3.objects.create(user=self.user3,
            Q48A = False, Q49A = True, Q50A = False, Q51A = True, Q52A = False, Q53A = False,
            Q54A = True, Q55A = False, Q56A = False, Q57A = False
        )
        do_set_available_stamps(self.user3.id, model_to_dict(c))
        profile = UserProfile.objects.get(user=self.user3)
        profile.filled_claims = 3
        profile.save()

        self.user4 = User.objects.create_user(username='user4', password='12345')
        c = Claim1.objects.create(user=self.user4,
            Q1A = True, Q2A = False, Q3A = False, Q4A = True, Q5A = False, Q6A = True,
            Q7A = True, Q8A = False, Q9A = False, Q10A = True, Q11A = False, Q12A = False,
            Q13A = True, Q14A = True, Q15A = False, Q16A = False, Q17A = False, Q18A = False,
            Q19A = True, Q20A = False, Q21A = False, Q22A = ['0', '1', '3'], Q23A = 1,
            Q24A = False, Q25A = False, Q26A = ['3', '4'], Q27A = ['0'], Q28A = ['4','7','9','10']
        )
        do_set_available_stamps(self.user4.id, model_to_dict(c))
        c = Claim2.objects.create(user=self.user4,
            Q29A = False, Q30A = True, Q31A = False, Q32A = False, Q33A = False, Q34A = False,
            Q35A = False, Q36A = True, Q37A = False, Q38A = False, Q39A = True, Q40A = True,
            Q41A = False, Q42A = False, Q42B = False, Q43A = True, Q44A = True, Q44B = True,
            Q45A = False, Q46A = True, Q46B = True, Q47A = True, Q47B = False
        )
        do_set_available_stamps(self.user4.id, model_to_dict(c))
        c = Claim3.objects.create(user=self.user4,
            Q48A = False, Q49A = True, Q50A = False, Q51A = False, Q52A = False, Q53A = False,
            Q54A = False, Q55A = False, Q56A = False, Q57A = True
        )
        do_set_available_stamps(self.user4.id, model_to_dict(c))
        c = Claim4.objects.create(user=self.user4,
            Q58A = True, Q59A = False, Q60A = False, Q61A = False, Q62A = False, Q63A = True,
            Q64A = False, Q65A = False, Q66A = True, Q67A = True, Q68A = False, Q69A = False,
            Q70A = False, Q71A = False, Q72A = False, Q73A = True, Q74A = False, Q75A = False,
            Q76A = False, Q77A = True, Q78A = False, Q78B = False, Q79A = False, Q79B = False,
            Q80A = True, Q81A = True, Q81B = True, Q82A = False, Q83A = False, Q84A = True,
            Q85A = True, Q86A = False, Q86B = True, Q87A = False, Q87B = False, Q88A = True,
            Q89A = False
        )
        do_set_available_stamps(self.user4.id, model_to_dict(c))
        profile = UserProfile.objects.get(user=self.user4)
        profile.filled_claims = 3
        profile.save()

    def test_check_available_stamps(self):
        print(UserProfile.objects.get(user=self.user1).stamp_count)
        print(UserProfile.objects.get(user=self.user2).stamp_count)
        print(UserProfile.objects.get(user=self.user3).stamp_count)
        print(UserProfile.objects.get(user=self.user4).stamp_count)

