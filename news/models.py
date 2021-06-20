from django.db import models
import datetime

class Articles(models.Model):
  title = models.CharField("Название", max_length=50, null=None)
  subtitle = models.CharField("Заголовок", max_length=250, null=None)
  text = models.TextField("Содержание", null=None)
  date = models.DateTimeField("Дата", default=datetime.datetime.now, blank=True, null=None)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return f"/news/{self.id}"

  class Meta:
    verbose_name = "Новость"
    verbose_name_plural = "Новости"
