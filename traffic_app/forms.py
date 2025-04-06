from django import forms
from .models import TrafficLightConfiguration

class TrafficLightForm(forms.ModelForm):
    class Meta:
        model = TrafficLightConfiguration
        fields = ['red_duration', 'yellow_duration', 'green_duration', 'current_state']
        widgets = {
            'red_duration': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control'
            }),
            'yellow_duration': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control'
            }),
            'green_duration': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control'
            }),
            'current_state': forms.Select(attrs={'class': 'form-control'}),
        }