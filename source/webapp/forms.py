from django import forms
from webapp.models import Picture, Album


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image', 'signature', 'is_private']
        exclude = ['author']
        widgets = {
            'signature': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'is_private': forms.CheckboxInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'is_private']
        exclude = ['author']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'is_private': forms.CheckboxInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
