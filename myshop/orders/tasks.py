from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully
    created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Hello {order.first_name}, \n \nYou have successfully \
                placed an order. Your order id is {order.id}."
    
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent

    # To start celery from terminal type: celery -A myshop worker -l info
    # Docs for celery: http://docs.celeryproject.org/en/latest/index.html    

    # To start rabbitMq: sudo systemctl start rabbitmq-server ,
    # for stoping rabbitmq-server instead start type stop.
    # listen on port 15672, after you run Celery from previous comand
    # Docs for rabbitMq: https://www.rabbitmq.com/download.html

    # To start flower from terminla type: celery -A myshop flower,
    # listen on port 5555, after you run Celery from command before last
    # Docs for flower: https://flower.readthedocs.io/en/latest/