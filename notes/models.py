from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):   
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    note = models.CharField(max_length = 1000, null = True,blank=True)
    file = models.FileField(upload_to="files/", null = True,blank=True)
    recipent = models.ManyToManyField(User,related_name ="reciedved_notes",null = True, blank = True)
    def __unicode__(self):
        return self.note
    def __str__ (self):
        return f'{self.id} -- {self.owner}'