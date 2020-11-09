from django import forms
from .models import Dcorporate,Dwedding,Dbirthday,specialupload,Review,register,adminregister


#class CorporateForm(forms.ModelForm):
 #   class Meta:
  #      model=Corporate
   #     fields='__all__'

class DcorporateForm(forms.ModelForm):
    class Meta:
        model=Dcorporate
        fields='__all__'

class DweddingForm(forms.ModelForm):
    class Meta:
        model=Dwedding
        fields='__all__'

class DbirthdayForm(forms.ModelForm):
    class Meta:
        model=Dbirthday
        fields='__all__'

class specialuploadform(forms.ModelForm):
    class Meta:
        model=specialupload
        fields='__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

class registerform(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'


class adminregisterform(forms.ModelForm):
    class Meta:
        model=adminregister
        fields='__all__'