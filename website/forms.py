from django import forms

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
