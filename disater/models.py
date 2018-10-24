from django.db import models

#person
class person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    profile_picture=models.CharField(max_length=50)

    def  __str__(self):
        return self.first_name+'-'+self.last_name
