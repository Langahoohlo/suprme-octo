from django import forms

from django import forms
from django.db.models import Q

from .models import MyMedia

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewMediaForm(forms.ModelForm):
    class Meta:
        model = MyMedia
        fields = ('image', 'video')

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        # Check if both fields are empty (null)
        if not image and not video:
            raise forms.ValidationError("Either image or video must be provided, but not both.")

        # Check if both fields are filled (not null)
        # if image and video:
        #     raise forms.ValidationError("Only one of image or video can be provided, not both.")

        return cleaned_data
