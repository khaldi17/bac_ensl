from django.db import models

class BacRegistration(models.Model):
    SPECIALITY_CHOICES = [
        ('sc', 'علوم تجريبية'),
        ('math', 'رياضيات'),
        ('mt', 'تقني رياضي'),
        ('lit', 'آداب'),
    ]

    STATUS_CHOICES = [
        ('pending', 'قيد المراجعة'),
        ('accepted', 'مقبول'),
        ('rejected', 'مرفوض'),
    ]

    username = models.BigIntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=10, choices=SPECIALITY_CHOICES)
    phone = models.CharField(max_length=10, null=True, blank=True)
    payment_receipt = models.FileField(upload_to='receipts/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_speciality_display()})"
    

