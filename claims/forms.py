from django import forms
from claims.models import Claim1, Claim2, Claim3, Claim4

class Claim1Form(forms.ModelForm):
    class Meta:
        model = Claim1
        fields = [
            'Q1A',
            'Q2A',
            'Q3A',
            'Q4A',
            'Q5A',
            'Q6A',
            'Q7A',
            'Q8A',
            'Q9A',
            'Q10A',
            'Q11A',
            'Q12A',
            'Q13A',
            'Q14A',
            'Q15A',
            'Q16A',
            'Q17A',
            'Q18A',
            'Q19A',
            'Q20A',
            'Q21A',
            'Q22A',
            'Q23A',
            'Q24A',
            'Q25A',
            'Q26A',
            'Q27A',
            'Q28A']
        widgets = {k: forms.RadioSelect(attrs={"required": "required"}) for k in
            ['Q1A',
            'Q2A',
            'Q3A',
            'Q4A',
            'Q5A',
            'Q6A',
            'Q7A',
            'Q8A',
            'Q9A',
            'Q10A',
            'Q11A',
            'Q12A',
            'Q13A',
            'Q14A',
            'Q15A',
            'Q16A',
            'Q17A',
            'Q18A',
            'Q19A',
            'Q20A',
            'Q21A',
            'Q23A',
            'Q24A',
            'Q25A']
        }

class Claim2Form(forms.ModelForm):
    class Meta:
        model = Claim2
        fields = [
            'Q29A',
            'Q30A',
            'Q31A',
            'Q32A',
            'Q33A',
            'Q34A',
            'Q35A',
            'Q36A',
            'Q37A',
            'Q38A',
            'Q39A',
            'Q40A',
            'Q41A',
            'Q42A',
            'Q42B',
            'Q43A',
            'Q44A',
            'Q44B',
            'Q45A',
            'Q46A',
            'Q46B',
            'Q47A',
            'Q47B']
        widgets = {k: forms.RadioSelect(attrs={"required": "required"}) for k in
            ['Q29A',
            'Q30A',
            'Q31A',
            'Q32A',
            'Q33A',
            'Q34A',
            'Q35A',
            'Q36A',
            'Q37A',
            'Q38A',
            'Q39A',
            'Q40A',
            'Q41A',
            'Q42A',
            'Q42B',
            'Q43A',
            'Q44A',
            'Q44B',
            'Q45A',
            'Q46A',
            'Q46B',
            'Q47A',
            'Q47B']
        }
class Claim3Form(forms.ModelForm):
    class Meta:
        model = Claim3
        fields = [
            'Q48A',
            'Q49A',
            'Q50A',
            'Q51A',
            'Q52A',
            'Q53A',
            'Q54A',
            'Q55A',
            'Q56A',
            'Q57A']
        widgets = {k: forms.RadioSelect(attrs={"required": "required"}) for k in
            ['Q48A',
            'Q49A',
            'Q50A',
            'Q51A',
            'Q52A',
            'Q53A',
            'Q54A',
            'Q55A',
            'Q56A',
            'Q57A']
        }

class Claim4Form(forms.ModelForm):
    class Meta:
        model = Claim4
        fields = [
            'Q58A',
            'Q59A',
            'Q60A',
            'Q61A',
            'Q62A',
            'Q63A',
            'Q64A',
            'Q65A',
            'Q66A',
            'Q67A',
            'Q68A',
            'Q69A',
            'Q70A',
            'Q71A',
            'Q72A',
            'Q73A',
            'Q74A',
            'Q75A',
            'Q76A',
            'Q77A',
            'Q78A',
            'Q78B',
            'Q79A',
            'Q79B',
            'Q80A',
            'Q81A',
            'Q81B',
            'Q82A',
            'Q83A',
            'Q84A',
            'Q85A',
            'Q86A',
            'Q86B',
            'Q87A',
            'Q87B',
            'Q88A',
            'Q89A']
        widgets = {k: forms.RadioSelect(attrs={"required": "required"}) for k in
            ['Q58A',
            'Q59A',
            'Q60A',
            'Q61A',
            'Q62A',
            'Q63A',
            'Q64A',
            'Q65A',
            'Q66A',
            'Q67A',
            'Q68A',
            'Q69A',
            'Q70A',
            'Q71A',
            'Q72A',
            'Q73A',
            'Q74A',
            'Q75A',
            'Q76A',
            'Q77A',
            'Q78A',
            'Q78B',
            'Q79A',
            'Q79B',
            'Q80A',
            'Q81A',
            'Q81B',
            'Q82A',
            'Q83A',
            'Q84A',
            'Q85A',
            'Q86A',
            'Q86B',
            'Q87A',
            'Q87B',
            'Q88A',
            'Q89A']
        }
