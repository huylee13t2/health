from time import time

from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext, ugettext_lazy as _

from account.models import CWGHMOUser
from healthstone.settings import PASSWORD_MIN_CHARS



def generate_user_code(user_id):
    ''' This  is implementation can change if there is a unique way the user code should be generated'''
    return u'%s%s' % (user_id, (int(time()) - 99999999))


class LoginForm(forms.Form):
    username = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder' :'Email', 'class': 'input-txt'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder' :'Password', 'class': 'input-txt'}))

    class Meta:
        fields = ('username', 'password')


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(initial='' ,max_length=100,  widget=forms.TextInput(attrs={'placeholder' :'First Name', 'class' :'input-txt'}))
    last_name = forms.CharField(initial='' ,max_length=100, label='Surname' , widget=forms.TextInput(attrs={'placeholder' :'Surname', 'class' :'input-txt'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput
        (attrs={'placeholder' :'Will be your username', 'class': 'input-txt'}))
    confirm_password = forms.CharField(label="Password" ,widget=forms.PasswordInput
        (attrs={'placeholder' :'Password', 'class' :'input-txt'}))
    password = forms.CharField(label="Confirm Password" ,widget=forms.PasswordInput
        (attrs={'placeholder' :'Confirm Password (min of %s characters)' % PASSWORD_MIN_CHARS, 'class' :'input-txt'}))

    class Meta:
        model = CWGHMOUser
        fields = ['first_name','last_name','middle_name','email','confirm_password','password','account_type']

        widgets = {
            'middle_name':forms.TextInput(attrs={'class':'input-txt', 'placeholder':'Middle Name'}),
            'account_type':forms.Select(attrs={'class':'form-part'}),
        }

    error_messages = {
        'short_password': _("The password is too short, minimum of %s characters." % PASSWORD_MIN_CHARS),
        'user_exists': _("This email address is already associated with an account with us, use the forgot password to recover it."),
        'password_mismatch': _("The password and password confirmation do not match."),
    }

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(username=email)
        if user:
            raise forms.ValidationError(
                self.error_messages['user_exists'],
                code='user_exists',
            )
        return email

    def clean_password(self):
        password = str(self.cleaned_data.get('password'))
        confirm_password = str(self.cleaned_data.get('confirm_password'))
        val_errors = []
        if len(password) < PASSWORD_MIN_CHARS:
            val_errors.append(forms.ValidationError(self.error_messages['short_password'], code='short_password'))
        if password != confirm_password:
            val_errors.append(forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch'))
        if val_errors:
            raise forms.ValidationError(val_errors)
        return password

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['email'], self.cleaned_data['email'], self.cleaned_data['password'])
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        ''' If there would be email verification, user acount have to be in inactive state until the user verify his/her email'''
        # user.is_active = False
        user.save()
        cwguser = super(RegisterForm, self).save(commit=False)
        cwguser.user = user
        cwguser.user_code = generate_user_code(user.id)
        if commit:
            cwguser.save()
        return cwguser
