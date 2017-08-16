from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'zamówienie nr {}'.format(order_id)
    message= 'Witaj {}!\n\n Przyjęliśmy Twoje zamówienie w naszym sklepie.\nIdentyfikator zamówienia to {}.'.format(order.first_name, order_id)

    mail_sent = send_mail(subject=subject,
                          message=message,
                          from_email='czapowski.piotr92@gmail.com',
                          recipient_list=[order.email])
    return mail_sent