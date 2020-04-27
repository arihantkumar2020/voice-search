from django.db import models

# Create your models here.


#model to create a table having all the attributes for Usersearches class
class UserSearches(models.Model):

    search_input = models.CharField(max_length=300)
    search_datetime = models.CharField(max_length=300)
