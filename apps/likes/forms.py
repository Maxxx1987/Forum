from django import forms

from apps.likes.models import Like


class AddLikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ('comment',)
        widgets = {
            'comment': forms.HiddenInput(),
        }

    def save(self, commit=True):
        user_id = self.instance.user_id
        comment_id = self.instance.comment_id
        like = Like.objects.filter(user_id=user_id, comment_id=comment_id).first()
        if like:
            like.delete()
            return like
        return Like.objects.create(user_id=user_id, comment_id=comment_id)
