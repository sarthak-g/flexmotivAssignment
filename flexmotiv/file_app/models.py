from django.db import models

# Create your models here.
class File(models.Model):
    file_title = models.CharField(max_length=30,blank=False)
    uploaded_file = models.FileField(upload_to="document_file",max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title
