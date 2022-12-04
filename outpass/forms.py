from django import forms
from captcha.fields import ReCaptchaField

class OutpassForm(forms.Form):
    name=forms.CharField(
        max_length=50,
        required=False,
        label='Name',
        )
    
    roll_number=forms.CharField(max_length=50,required=False,label='Roll Number')
    
    email=forms.EmailField(required=False,label='Email')
    
    # captcha = ReCaptchaField()
    