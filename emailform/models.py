from django.db import models

class Post(models.Model):
  text = models.TextField(null=True, max_length=255)
  updated = models.DateTimeField(null=True, auto_now=True)
  created = models.DateTimeField(null=True, auto_now_add=True)

  class Meta:
      ordering = ['created']

  #first = models.CharField(max_length=50)
  #last = models.CharField(max_length=50)
  #email = models.EmailField(max_length=254)
  #created_date = models.DateTimeField(default=timezone.now)

  #def publish(self):
  #  self.created_date()
  #  self.save()

  #def __str__(self):
   # return self.email
