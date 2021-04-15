from django.db import models


class Message(models.Model):
    email = models.EmailField(verbose_name='email', max_length=50)
    text = models.CharField(verbose_name='text', max_length=100)
    create_at = models.DateTimeField(verbose_name='create_at', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='update_at', auto_now=True)
