import logging

from celery.app import shared_task

from lesson.models import LessonVenue

logger = logging.getLogger(__name__)


@shared_task
def send_student_active_lesson_task(lesson_pk):
    logger.info(f'send_student_active_lesson_task pk:{lesson_pk}...')
    LessonVenue.send_student_active_lesson(lesson_pk)
    logger.info(f'send_student_active_lesson_task done.')
    return True
