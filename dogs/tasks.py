from celery import shared_task
from django.conf import settings

from django.core.mail import send_mail
from django.utils import timezone

from dogs.models import Dog


@shared_task
def send_birthday_messages_task():
    dogs = Dog.objects.filter(birth_day=timezone.now().date())

    for dog in dogs:
        send_mail(
            subject='Happy birthday',
            message='Happy birthday',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[dog.owner.email],
        )


