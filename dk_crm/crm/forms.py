from django import forms

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=None, required=True)
    password = forms.CharField(max_length=None, required=True, widget=forms.PasswordInput)

class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    text = forms.CharField(max_length=200, required=True, widget=forms.Textarea)

