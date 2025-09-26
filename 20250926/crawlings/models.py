from django.db import models

# Create your models here.
class Crawling(models.Model):
    company_name = models.CharField()
    code = models.CharField()
    comment = models.CharField()
    saved_at = models.DateTimeField(auto_now_add=True)