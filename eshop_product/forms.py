from django.forms import ModelForm

from eshop_product.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']