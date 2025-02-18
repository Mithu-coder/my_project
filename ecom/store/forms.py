from django import forms
from store.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','age','photo']
        