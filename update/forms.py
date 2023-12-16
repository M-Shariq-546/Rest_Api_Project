from django import forms 
from .models import update as UpdateModel

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = ['user', 'content', 'image']
        
    def clean(self , *args , **kwargs):
        data = self.cleaned_data
        content = data.get('content')
        if content == "":
            content = None
        image = data.get('image')
        if image == "":
            image = None
            
        if content is None and image is None:
            raise forms.ValidationError("Content or image is missing. Please check entered data")
        
        return super().clean(*args, **kwargs)
        