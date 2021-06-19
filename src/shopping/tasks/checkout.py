import logging

from celery.app import shared_task
from django.shortcuts import get_object_or_404
from course.models import Participation

logger = logging.getLogger(__name__)


@shared_task
def create_user_after_checkout(order_id):
    logger.info(f'create_user_after_checkout  order:{order_id}...')
    from shopping.models import Bestellung
    order = get_object_or_404(Bestellung, pk=order_id)
    
    course = order.product.course
    user = order.create_user_from_order()
    Participation.objects.get_or_create(
        user=user,
        course=course
        )
    user.send_new_user_email(order_id)
    
    logger.info(f'done.')
    
