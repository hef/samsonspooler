from django.db import models

# Create your models here.

class PrintJob(models.Model):
	filename = models.CharField(max_length=64)
	submitted = models.DateField()
	started = models.DateField()
	finished = models.DateField()

