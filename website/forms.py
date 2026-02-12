from django import forms
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
            "height": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 100,
                "max": 250
            }),
            "procedure_of_interest": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "weight_to_lose": forms.NumberInput(attrs={
                "class": "form-control"
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

class ContactForm(forms.Form):
    contactName = forms.CharField(
        max_length=100,
        label="Name"
    )
    contactEmail = forms.EmailField(
        label="Email"
    )
    contactPhone = forms.CharField(
        max_length=20,
        required=False,
        label="Phone"
    )
    contactReason = forms.ChoiceField(
        choices=[
            ("appointment", "Schedule an Appointment"),
            ("question", "General Question"),
            ("feedback", "Feedback or Suggestion"),
            ("international", "International Patient Inquiry"),
            ("other", "Other"),
        ],
        label="Reason for contact"
    )
    contactMessage = forms.CharField(
        widget=forms.Textarea,
        label="Message"
    )