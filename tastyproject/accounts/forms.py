from django import forms
# from django.forms import Modelform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser

# class RegisterForm(forms.ModelForm):
#     password=forms.CharField(label='Password',widget=forms.PasswordInput)
#     password2= forms.CharField(label='Reapeat Password', widget=forms.PasswordInput)
#     class Meta:
#         Model=User
#         fields=['username']

#     def clean_password2(self):
#         cd=self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError('Passwords not mached!')
#         return cd['password2']



# class UserForm(UserCreationForm):
    
#     class Meta:
#         model=MyUser
#         fields='__all__'






# class UserForm(UserCreationForm):   #RegiUser
#     M_or_F=(
#         ('남자','남자'),
#         ('여자','여자'),
#         ('중성','중성'),
#     )
#     email= forms.EmailField(label="email")
#     gender=forms.CharField( max_length=2, required=False)
#     birth= forms.DateField()
#     # user = forms.OneToOneField(User, on_delete=forms.CASCADE)
#     #회원가입 내용에 첨부하고 싶은거
#     # gender= forms.CharField(choices=M_or_F, max_length=2, null=True)   #null=False로???
#     # birth= forms.DateField(null=True)

#     class Meta:
#         model=User
#         fields=("username", "email", "gender", "birth")

