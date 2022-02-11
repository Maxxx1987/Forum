from django import forms


class AddTopicForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
