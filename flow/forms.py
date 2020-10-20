 
from django import forms
from .models import Image

class NewPostForm(forms.ModelForm):
    '''
    Form for a user to create a new form
    '''
    class Meta:
        model = Image
        exclude = ['image_poster']
        # fields = ('image_name', 'image', 'image_caption')

