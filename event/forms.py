from django import forms
from .models import Event, Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class EventForm(forms.ModelForm):
    is_published = forms.BooleanField(label='Published', required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'date', 'time', 'max_capacity', 'location', 'is_published']
        widgets = {
            'date': DatePickerInput(attrs={'class': 'form-control'}),
            'time': TimePickerInput(attrs={'class': 'form-control'}),
        }
        

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event_name', 'date', 'start_time', 'end_time']
        widgets = {
            'date': DatePickerInput(attrs={'class': 'form-control'}),
            'start_time': TimePickerInput(attrs={'class': 'form-control'}),
        }