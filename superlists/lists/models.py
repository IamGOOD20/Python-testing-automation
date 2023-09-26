from django.db import models

class Item(models.Model):
    '''Item of list'''
    text = models.TextField(default='')
