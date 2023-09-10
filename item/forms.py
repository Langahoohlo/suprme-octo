from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'phone', 'image', 'area', 'city')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'area': forms.TextInput(attrs={  # Add the widget for the 'area' field
                'class': INPUT_CLASSES,
            }),
            'city': forms.Select(attrs={  # Add the widget for the 'area' field
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'phone', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class ItemVerificationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['is_verified']  # Include only the field you want to customize

    # Customize the label for the is_verified field
    is_verified = forms.BooleanField(
        required=False,
        label="Available",  # This sets the label to "Available" in the form
    )

