from django.db import models
from django import forms

# Create your models here.

class PrintJob(models.Model):
	title = models.CharField(max_length=64)
	submitted = models.DateTimeField()
	created = models.DateTimeField(null=True, blank=True)
	finished = models.DateTimeField(null=True, blank=True)
        gcode = models.FileField(upload_to="gcode")

        def __unicode__(self):
            return self.title

class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
        exclude = ('submitted', 'created', 'finished')
