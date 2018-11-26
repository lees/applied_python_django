from django.forms import ModelForm, HiddenInput
from forum.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['author_nick', 'text', 'topic']
		widgets = {
			'topic': HiddenInput()
		}
