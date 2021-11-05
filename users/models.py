from django.db import models

from support_system.models import Ticket


class UserQuestion(models.Model):
    """ User message """

    answer = models.TextField(verbose_name='Вопрос пользователя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')
    ticket = models.ForeignKey(Ticket, blank=True, null=True, related_name='user_ask', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_question'
        verbose_name = "Вопрос пользователя"
        verbose_name_plural = "Пользовательские вопросы"
