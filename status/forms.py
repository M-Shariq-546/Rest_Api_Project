from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['user', 'content', 'image']
    
    def clean_content(self , *args , **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 200:
            raise forms.ValidationError('Content is too Long. Please Post Less tha 200 Characters')
        return content
    
        
    def clean(self , *args , **kwargs):
        data = self.cleaned_data
        content = data.get('content')
        if content == "":
            content = None
        image = data.get('image')
        if image == "":
            image = None
            
        if content is None and image is None:
            raise forms.ValidationError("Content or image is missing. Please entered data")
        
        return super().clean(*args, **kwargs)
        