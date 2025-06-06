from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class ProducerVerify(models.Model):
        id = models.AutoField(primary_key=True)
        firstName= models.CharField(max_length=20,null=True)
        lastName= models.CharField(max_length=20,null=True)
        email= models.EmailField(null=True)
        contact=models.CharField(max_length=20,null=True)
        postalcode=models.CharField(max_length=10,null=True)
        address= models.CharField(max_length=110,null=True)
        pictures = models.FileField(upload_to='producer_pictures', blank=True, null=True)
        document = models.FileField(upload_to='producer_documents', null=True, blank=True)
        verified = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True,null=True)

        class meta:
            # ascending order in first name
            ordering=['firstName']
            # database index for producer account
            indexes = [
                        models.Index(fields=['firstName']),
                        ]
        def delete(self, *args, **kwargs):
            # Delete associated picture file from the filesystem
            if self.pictures:
                os.remove(self.pictures.path)
            # Delete associated document file from the filesystem
            if self.document:
                os.remove(self.document.path)
            super().delete(*args, **kwargs)


class Producer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
        id = models.AutoField(primary_key=True)
        firstName= models.CharField(max_length=20,null=True)
        lastName= models.CharField(max_length=20,null=True)
        email= models.EmailField(null=True)
        contact=models.CharField(max_length=20,null=True)
        postalcode=models.CharField(max_length=10,null=True)
        address= models.CharField(max_length=110,null=True)
        pictures = models.FileField(upload_to='producer_pictures', blank=True, null=True)
        document = models.FileField(upload_to='producer_documents', null=True, blank=True)
        verified = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True,null=True)

        class meta:
            # ascending order in first name
            ordering=['firstName']
            # database index for producer account
            indexes = [
                        models.Index(fields=['firstName']),
                        ]
        def delete(self, *args, **kwargs):
            # Delete associated picture file from the filesystem
            if self.pictures:
                os.remove(self.pictures.path)
            # Delete associated document file from the filesystem
            if self.document:
                os.remove(self.document.path)
            super().delete(*args, **kwargs)
