from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields=[
            'PersonName',
            'Person_sex',
            'Person_BDate'
        ]

    def clean_personname(self,*args,**kwargs):
        personname = self.clean_data.get('PersonName')
        if len(personname) > 30:
            raise forms.ValidationError("Person Name too long should be less then 30")
        

    def clean_validate(self,*args,**kwargs):
        data = self.cleaned_data
        personname = data.get('PersonName',None)
        if personname == "":
            personname = None
        personsex = data.get('Person_sex',None)
        if personsex == "":
            personsex = None
        personbdate = data.get('Person_BDate',Non)
        if personbdate =="":
            personbdate = None

        if personbdate is None or personsex is None or personname is None:
            raise forms.ValidationError("PersonName or PersonSEx or PersonBDate is missing")
        return super.clean_validate(*args,**kwargs)



