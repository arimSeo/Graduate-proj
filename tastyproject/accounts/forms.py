from django import forms
from django.contrib.auth.models import User
from .models import MyUser
from django.core.exceptions import ValidationError
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class RegisterForm(forms.ModelForm):
    class Meta:
        model= MyUser
        fields=['gender']
        widgets={
            'gender': forms.Select(attrs={
            'class': "gen-form",
            'style': 'border-top:0; border-left: 0; border-right: 0; border-bottom: 1.4px solid #ED7D31; background:transparent; outline:none;  width:168px;'
            })            
        }
    # def clean(self):
    #     cleaned_data = super.clean()
    #     name = self.cleaned_data.get('name')
    #     print(name)
    #     if MyUser.objects.filter(name=name).exist():
    #         raise forms.ValidationError('이미 존재하는 아이디입니다.')
       
