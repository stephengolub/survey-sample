from django.conf import settings
from django.contrib import admin
from django.db import models


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    available_options = models.ManyToManyField(Choice)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    responder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    captured_at = models.DateTimeField(auto_now_add=True)

    @property
    def answer_text(self):
        return self.answer.choice_text

    def __str__(self):
        return "{self.answer_text} ({self.question})".format(**locals())

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
