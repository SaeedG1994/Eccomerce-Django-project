from django.forms import  ModelForm,TextInput,Textarea
from .models import ContactMessage
from django import forms
#  THIS IS FORM USE FOR THE  ( CONTACT US  FUNCTION ) ON THE VIEWS
#_____________________________________________________________
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject','message']
        widgets ={
            'name' :TextInput(attrs={'class':'input','placeholder':'Name & surName'}),
            'email' :TextInput(attrs={'class':'input','placeholder':'Email Address'}),
            'subject' :TextInput(attrs={'class':'input','placeholder':'subject'}),
            'message' :Textarea(attrs={'class':'input','placeholder':'your Message','rows':'5'}),

        }



#  THIS IS FORM USE FOR THE  ( SEARCH FUNCTION ) ON THE VIEWS
#_____________________________________________________________

class SearchForm(forms.Form):
    query=forms.CharField(max_length=100)
    catid=forms.IntegerField()