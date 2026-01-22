from django.apps import AppConfig


class SchoolTransportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school_transport'

    def ready(self):
        from django.apps import AppConfig
        from django.db.models.signals import post_save

        class SchoolTransportConfig(AppConfig):
            default_auto_field = "django.db.models.BigAutoField"
            name = "school_transport"

            def ready(self):
                from .models import Child
                from django.contrib import messages
                from django.dispatch import receiver

                @receiver(post_save, sender=Child)
                def notify_driver(sender, instance, created, **kwargs):
                    if created and instance.driver:
                        # Here you can integrate real notifications (email, push, etc.)
                        print(f"New child {instance} assigned to driver {instance.driver}")

        import school_transport.signals