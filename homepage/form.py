from django import forms
from .models import Main
#Retirive and Validate here

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ["Title"]
    def clean_Title(self):
        obj = self.cleaned_data.get("Title")
        if(len(obj)>20 or len(obj)<5):
            raise forms.ValidationError("Len Error")
        return obj 
        
