# your_app/forms/hospital_form.py
from django import forms
from .models import Hospital,Department

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'department']

    # Override the default department field to use ModelMultipleChoiceField
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Make it optional if needed
    )
