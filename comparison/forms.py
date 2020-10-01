from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class FilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices_chipset = kwargs.pop('choices_chipset')
        choices_benchmark = kwargs.pop('choices_benchmark')
        super(FilterForm, self).__init__(*args, **kwargs)

        self.fields["Chipset"] = forms.MultipleChoiceField(choices=choices_chipset,
                                                           widget=forms.CheckboxSelectMultiple(), required=True)
        self.fields["Benchmark"] = forms.MultipleChoiceField(choices=choices_benchmark,
                                                             widget=forms.CheckboxSelectMultiple(), required=True)
