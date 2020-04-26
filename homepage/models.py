from django.db import models

# Create your models here.

class UserSearches(models.Model):

    search_input = models.CharField(max_length=300)
    search_date = models.DateField()
    search_time = models.TimeField()
    search_count = models.IntegerField()
