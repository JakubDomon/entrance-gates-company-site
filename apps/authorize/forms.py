from django import forms

# Login Form
class LoginForm(forms.Form):
    attr = {'class': 'w-75 mb-3'}

    user_name = forms.CharField(label='Login', max_length=25, widget=forms.TextInput(attrs=attr))
    password = forms.CharField(label='Hasło', max_length=50, widget=forms.PasswordInput(attrs=attr))

class RegisterForm(forms.Form):
    attr = {'class': 'w-100 mb-3'}

    user_name = forms.CharField(label='Nazwa użytkownika', max_length=25, widget=forms.TextInput(attrs=attr))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=attr))
    password = forms.CharField(label='Hasło', max_length=50, min_length=5, widget=forms.PasswordInput(attrs=attr))
