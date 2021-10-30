from django.db import models
from support_system.models import Ticket


class UserAsks(models.Model):
    """ User message """

    answer = models.TextField(verbose_name='Вопрос пользователя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')
    ticket = models.ForeignKey(Ticket, blank=True, null=True, related_name='user_ask', on_delete=models.CASCADE)
