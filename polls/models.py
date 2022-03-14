import uuid
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s object (%s, %s)' % (self.__class__.__name__, self.pk, self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s object (%s, %s)' % (self.__class__.__name__, self.pk, self.choice_text)
