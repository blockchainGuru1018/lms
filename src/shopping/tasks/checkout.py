import logging

from celery.app import shared_task
from django.shortcuts import get_object_or_404



logger = logging.getLogger(__name__)


@shared_task
def create_user_after_checkout(order_id):
    logger.info(f'create_user_after_checkout  order:{order_id}...')
    from shopping.models import Bestellung
    order = get_object_or_404(Bestellung, pk=order_id)
    
    user = order.create_user_from_order()
    
    user.send_new_user_email()
    
    logger.info(f'done.')
    