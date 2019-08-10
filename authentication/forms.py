from django import forms
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username:",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'example:john,etc...'}))
    password = forms.CharField(label="Password:",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This username does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong password")
            if not user.is_active:
                raise forms.ValidationError("This username does not active")
        return super(UserLoginForm, self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    email    = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

        def clean_email(self):
            email = self.cleaned_data.get('email')

            email_qs = User.objects.filter(email=email)
            if email_qs.exist():
                raise forms.ValidationError("This email already being used")
            return email
