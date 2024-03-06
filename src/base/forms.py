from django import forms
from .models import Question, Option


class NumberForm(forms.Form):
    first_num = forms.IntegerField(label="Birinchi son", required=True)
    second_num = forms.IntegerField(label="Ikkinchi son", required=True)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]
        exclude = ["created_date"]


class AllForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    first_name = forms.CharField(max_length=50, label='First Name')
    age = forms.IntegerField(min_value=18, label='Age')
    country = forms.CharField(max_length=50, label='Country')
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], label='Gender')
    agree_terms = forms.BooleanField(label='Agree to Terms and Conditions')


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'question']
