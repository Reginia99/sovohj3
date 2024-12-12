from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'location'] 

from .models import Picture
class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']  # Only the image field