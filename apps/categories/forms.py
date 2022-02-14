from django import forms

from apps.categories.models import Topic


class AddTopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('name', 'description')
