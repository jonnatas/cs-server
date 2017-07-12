from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.utils import timezone

from codeschool import models as m

class Post(models.Model):
    author = models.ForeignKey(m.User, related_name='users')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '{}; Author:{} '.format(self.title, self.author.username)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey(m.User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '{}; Autor: {}'.format(self.text, self.author.username)