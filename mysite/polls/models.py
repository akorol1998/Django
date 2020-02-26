import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(verbose_name="date_published")

    def __str__(self):
        return f"{self.question_text}\n"

    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"

