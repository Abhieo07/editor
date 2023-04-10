from django.db import models
from datetime import datetime

# Create your models here.
class Core(models.Model):
    text = models.TextField(null=True,max_length=1000)
    video = models.FileField(upload_to='videos/',null=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{str(self.video)}' + self.text