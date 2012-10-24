from django.db import models
from django import forms

# Create your models here.

class PrintJob(models.Model):
	filename = models.CharField(max_length=64)
	submitted = models.DateField()
	started = models.DateField()
	finished = models.DateField()

        def __unicode__(self):
            return self.filename

class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
