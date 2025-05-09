from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import BacRegistration

@receiver(pre_save, sender=BacRegistration)
def set_username_by_speciality(sender, instance, **kwargs):
    if instance.username is None:
        base_numbers = {
            'sc': 300000,
            'math': 400000,
            'lit': 500000,
        }
        base = base_numbers.get(instance.speciality, 600000)
        
        # عدّ الموجودين في نفس التخصص
        count = BacRegistration.objects.filter(speciality=instance.speciality).count()
        instance.username = base + count + 1
#

