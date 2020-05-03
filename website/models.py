from django.db import models

# Create your models here.
class ContactTickets(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=300)
    email=models.EmailField(default=None,blank=True)
    message=models.TextField()
    def __str__(self):
        return self.name
