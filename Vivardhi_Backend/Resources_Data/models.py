from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)
    working_hours = models.IntegerField()
    shift = models.CharField(max_length=50)
    allocated = models.BooleanField()

    class Meta:
        managed = False  
        db_table = 'SAMPLE_DATA' 

    def __str__(self):
        return self.name