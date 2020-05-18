from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    """docstring for Category"""
    name = models.CharField(max_length=100, help_text='Enter category')

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name    


class TodoList(models.Model):
    title = models.CharField(max_length=200, help_text='Enter title')
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="General", on_delete = models.SET_NULL, null=True)

    class Meta:
        ordering = ["-created"]


    def __str__(self):
        return self.title 

