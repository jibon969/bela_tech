from django import forms
from .models import Contact, Replay
from django.forms import Textarea
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'subject',
            'name',
            'phone',
            'email',
            'message',
        ]

        # Override the Customer some fields
        widgets = {
            'message': Textarea(attrs={'rows': 4, 'cols': 3}),
        }

    # Validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "hi":
            raise forms.ValidationError("Please provide valid name")
        if name == 1:
            raise forms.ValidationError("Please provide valid name")
        return name



class ReplayForm(forms.ModelForm):
    class Meta:
        model = Replay
        fields = [
            'send_to',
            'subject',
            'message',
        ]

        # Override the Customer some fields
        widgets = {
            'message': Textarea(attrs={'rows': 4, 'cols': 3}),
        }



