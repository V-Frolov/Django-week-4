from django import forms


class CreateBook(forms.Form):
    title = forms.CharField(max_length=128, label="Title great book:")
    description = forms.CharField(widget=forms.Textarea, label="Enter text here :")
    author_id = forms.IntegerField(label="Enter ID author")
    released_year = forms.IntegerField(label="When created :")
