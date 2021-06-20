from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
  class Meta:
    model = Articles
    fields = ["title", "subtitle", "text", "date"]

    widgets = {
      "title": TextInput(attrs={
        "placeholder": "Заголовок статьи"
      }),
      "subtitle": TextInput(attrs={
        "placeholder": "Подзаголовок статьи"
      }),
      "text": Textarea(attrs={
        "placeholder": "Содержание"
      }),
      "date": DateTimeInput(attrs={
        "placeholder": "Дата публикации"
      })
    }
