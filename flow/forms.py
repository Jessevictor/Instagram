from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image, Profile
from django.contrib.auth.models import User
class NewPostForm(forms.ModelForm):
    '''
    Form for a user to create a new form
    '''
    class Meta:
        model = Image
        exclude = ['image_poster']
        # fields = ('image_name', 'image', 'image_caption')
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = ['image']
