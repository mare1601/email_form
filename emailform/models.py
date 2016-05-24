from django.db import models
from django.utils import timezone

class Post(models.Model):
  first = models.CharField(max_length=50)
  last = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  created_date = models.DateTimeField(default=timezone.now)

  #def publish(self):
   # self.created_date()
    #self.save()

  #def __str__(self):
   # return self.email