from django import forms
from django.conf import settings

User = settings.AUTH_USER_MODEL

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    name = forms.CharField(label="Name")
    plan = forms.IntegerField(label="Plan")
    password = forms.CharField(label="Password")
    password_confirm = forms.CharField(label="Confirm Password")

    def clean(self):
        form_data = super().clean()
        try:
            User.objects.get(email=form_data['email'])
            self.add_error('email', "Email is already in use")
        except User.DoesNotExist:
            pass
        if form_data['password'] != form_data['password_confirm']:
            self.add_error(None, "Passwords do not match")
        return form_data
