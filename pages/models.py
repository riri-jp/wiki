from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'page_id': self.id})
