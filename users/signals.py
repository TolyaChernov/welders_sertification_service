from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import User

# @receiver(post_save, sender=User)
# def add_score(instance, **kwargs):
#     profile = instance.category
#     num = User.objects.filter(category__title=instance.category)
#     profile.score = num.count()
#     profile.save()


# @receiver(post_delete, sender=User)
# def del_score(instance, **kwargs):
#     profile = instance.category
#     # profile.score -= 1
#     # profile.save()
#     num = User.objects.filter(category__title=instance.category)
#     profile.score = num.count()
#     profile.save()


@receiver(post_save, sender=User)
def create_user_profile(instance, **kwargs):
    # if created:
    print(
        "*****************************************************************************************************************************************************************************************************************************************************************"
    )
    a = list(instance.groups.all())
    print(a)
    if len(a) == 0:
        instance.groups.add(Group.objects.get(name="customer"))
    a = list(instance.groups.all())
    print(a)
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
