from django import forms
from .models import Contact
class AppointmentForm(forms.ModelForm):

    class Meta:
        exclude = ["created_at"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full name"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 10,
                "max": 100
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+1 555 123 4567"
            }),
            "weight": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 20,
                "max": 500
            }),
            "weight_unit": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "height": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 100,
                "max": 250
            }),
            "height_unit": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "procedure_of_interest": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "weight_to_lose": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "weight_to_lose_unit": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "prev_surgeries": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "medical_conditions": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "medications": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "travel": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "forms_of_contact": forms.TextInput(attrs={
                "class": "form-control"
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "reason", "message"]