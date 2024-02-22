from django import forms






class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)




class SignupForm(forms.Form):
    username=forms.CharField(label='username',max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField(label='email',max_length=100)    
