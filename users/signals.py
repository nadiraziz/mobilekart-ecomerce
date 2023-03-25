from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
    
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

