from django import forms
from .models import Event
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'date', 'time', 'max_capacity', 'location']
        widgets = {
            'date': DatePickerInput(attrs={'class': 'form-control'}),
            'time': TimePickerInput(attrs={'class': 'form-control'}),
        }