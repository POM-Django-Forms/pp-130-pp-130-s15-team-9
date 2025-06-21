from django import forms
from .models import Author
from book.models import Book

class AuthorForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
            'size': 6
        })
    )

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic', 'books']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 20,
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 20,
                'required': True
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 20,
                'required': True
            }),
        }