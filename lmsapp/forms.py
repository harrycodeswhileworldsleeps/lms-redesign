from django import forms 
from .models import login ,quizmodel

class LoginForm(forms.ModelForm):
    class Meta:
        model=login 
        fields="__all__"
class QuizForm(forms.ModelForm):
    class Meta:
        model=quizmodel
        fields="__all__"

