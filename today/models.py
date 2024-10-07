from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField( max_length=50)
    details = models.TextField()
    file = models.FileField( upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True )
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name