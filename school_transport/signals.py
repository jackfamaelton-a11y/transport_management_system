from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Child, Notification

@receiver(post_save, sender=Child)
def notify_driver_new_child(sender, instance, created, **kwargs):
    """
    Notify the driver if a new child is assigned to them.
    """
    if created and instance.driver:
        Notification.objects.create(
            driver=instance.driver,
            message=f"You have been assigned a new child: {instance.full_name}."
        )