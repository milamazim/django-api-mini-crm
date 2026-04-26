from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20, unique=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name}"
    
