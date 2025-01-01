from django import forms
from .models import Patient, Survey

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_number']
        
class SurveySelectForm(forms.Form):
    survey_selected = forms.ModelChoiceField(
        queryset=Survey.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select a Survey",
        empty_label="Choose a survey"
    )
