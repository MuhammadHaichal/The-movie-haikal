from django import forms

class SearchMovie(forms.Form):
    title = forms.CharField(
            max_length=70,
            widget = forms.TextInput(
                attrs={
                    'placeholder' : 'drama',
                    'class' : 'form-control me-2',
                    }
                )
            )
    

