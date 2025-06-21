from django import forms
from .models import Order
from book.models import Book

class OrderForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Book'
    )
    plated_end_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        }),
        label='Planned return'
    )

    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']