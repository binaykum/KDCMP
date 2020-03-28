from django import forms
from .models import Complaints,Villagename

class complaints_form(forms.ModelForm):
    complainno = forms.CharField(widget=forms.TextInput, required=True, max_length=10)  
    #date = forms.DateField(widget=forms.DateField)
    subject = forms.CharField(widget=forms.TextInput, max_length=200)
    # villagename = forms. (widget=forms.TextInput, max_length=200 )  # Field name made lowercase.        
    actionby = forms.CharField(widget=forms.TextInput, required=False, max_length=10) 
    status = forms.CharField(widget=forms.TextInput, required=False, max_length=10) 
    remarks = forms.CharField(widget=forms.TextInput, required=False, max_length=10)
    slno = forms.IntegerField
    
    class Meta():
        model= Complaints
    #    fields=['slno', 'complainno','subject','villagename','actionby','status','remarks']
        fields = '__all__'
    

class village_form(forms.ModelForm):
    
    class Meta():
        model= Villagename
        fields='__all__'