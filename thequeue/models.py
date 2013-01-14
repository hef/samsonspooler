from django.db import models
from django import forms
from driver.tasks import print_s3g 
from StringIO import StringIO

# Create your models here.

class PrintJob(models.Model):
	title = models.CharField(max_length=64)
	submitted = models.DateTimeField()
	created = models.DateTimeField(null=True, blank=True)
	finished = models.DateTimeField(null=True, blank=True)
        s3g = models.FileField(upload_to="s3g")

        def __unicode__(self):
            return self.title

        def send(self):
            data = self.s3g.read()
            handle = StringIO(data)
            print_s3g.delay(handle)

class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
        exclude = ('submitted', 'created', 'finished')
