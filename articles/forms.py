from django import forms
from django.forms import HiddenInput

from .models import Article

class ArticleModelForm(forms.ModelForm):
	body = forms.Textarea


	hash = forms.CharField(widget=HiddenInput(), required=False)
	txId = forms.CharField(widget=HiddenInput(), required=False)

	class Meta:
		model = Article
		fields = ["body"]








