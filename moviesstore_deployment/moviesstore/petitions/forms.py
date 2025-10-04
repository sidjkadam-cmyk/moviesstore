from django import forms
from .models import MoviePetition

class MoviePetitionForm(forms.ModelForm):
    class Meta:
        model = MoviePetition
        fields = ['title', 'description', 'movie_title', 'year', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a catchy title for your petition'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Explain why this movie should be added to our catalog...'
            }),
            'movie_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the exact movie title'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 2023',
                'min': '1900',
                'max': '2030'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Action, Drama, Comedy (optional)'
            })
        }
        labels = {
            'title': 'Petition Title',
            'description': 'Description',
            'movie_title': 'Movie Title',
            'year': 'Release Year',
            'genre': 'Genre (Optional)'
        }
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year and (year < 1900 or year > 2030):
            raise forms.ValidationError('Please enter a valid year between 1900 and 2030.')
        return year
