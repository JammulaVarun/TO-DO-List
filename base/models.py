from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class todo_list(models.Model):
    
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'
    class Meta:
        ordering = ['is_complete']