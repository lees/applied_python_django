
from django.db import models

class Topic(models.Model):
    subject = models.CharField(u'Тема', max_length=255)
    text = models.TextField(u'Текст')
    creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    def __str__(self):
        return '{} | {}'.format(self.pk, self.subject)

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    author_nick   = models.CharField(u'Автор', max_length=255)
    text = models.TextField(u'Текст')
    reply_to = models.ForeignKey('forum.Comment', null=True, blank=True, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    def __str__(self):
        return "{} -> {}".format(self.author_nick, self.topic)
