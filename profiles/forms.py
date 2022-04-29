from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import UserProfile, Stamps
import heapq


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.selected_stamps is not None and self.instance.stamp_count is not None:
            # produce list of tuples with (key,value) of largest count
            most_stamps = heapq.nlargest(3, self.instance.stamp_count.items(), key=lambda x: x[1])
            choices = [Stamps.choices[int(v[0])] for v in most_stamps]
            self.fields['selected_stamps'].choices = choices
            self.fields['selected_stamps'].widget.choices = choices

    class Meta:
        model = UserProfile
        fields = [
            'selected_stamps',
            'first_name',
            'last_name',
            'age',
            'gender',
            'sexual_orientation',
            'location_city',
            'location_state',
            'location_country',
            'education',
            'user_avatar',
            'religion',
            'children',
            'destination',
            'question1',
            'question2',
            'question3',
            'question4',
            'question5',
            'question6']
        widgets = {
            'selected_stamps': forms.CheckboxSelectMultiple(attrs={'class': 'stamps-select'}),
            'gender': forms.RadioSelect(attrs={'class': 'radio-select gender'}),
            'sexual_orientation': forms.RadioSelect(attrs={'class': 'radio-select sexual-orientation'}),
            'education': forms.RadioSelect(attrs={'class': 'radio-select education'}),
            'religion': forms.CheckboxSelectMultiple(),
            'children': forms.CheckboxSelectMultiple(),
            'destination': forms.CheckboxSelectMultiple(),
        }
