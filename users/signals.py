from django.contrib.auth.models import Group, User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import User


@receiver(post_save, sender=User)
def create_user_profile(instance, **kwargs):
    a = list(instance.groups.all())
    if len(a) == 0:
        instance.groups.add(Group.objects.get(name="customer"))
        list_mail = []
        usermail = str(instance.email)
        list_mail.append(usermail)
        message_text = """Приветствуем Вас на нашем сервисе и благодарим за регистрацию. На сайте Вы можете сделать заявку и отслеживать ее статус"""
        send_mail(
            "WELCOME",
            message_text,
            "support@example.com",
            list_mail,
            fail_silently=False,
        )
