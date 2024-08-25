from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='URL', required=True)

    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'class': 'form-control'})

