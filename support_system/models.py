from django.contrib.auth.models import User
from django.db import models


class StatusTicket(models.Model):
    """ Ticket statuses: resolved, unresolved, frozen """

    name = models.CharField(max_length=125, verbose_name='Статус тикета')

    class Meta:
        db_table = 'status_ticket'
        verbose_name = " Статус тикета"
        verbose_name_plural = "Статусы тикетов"

    def __str__(self):
        return f'{self.id}. {self.name}'


class Ticket(models.Model):
    """ Description of the Ticket model """

    class StatusTicket(models.TextChoices):
        TF = 1, 'Тикет заморожен'
        TR = 2, 'Тикет решен'
        TU = 3, 'Тикет не решен'

    title = models.CharField(max_length=125, blank=True, default='Без названия', verbose_name='Название тикета')
    content = models.TextField(verbose_name='Содержание тикета')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    status_ticket = models.CharField(max_length=2, verbose_name='Статус тикета', choices=StatusTicket.choices,
                                     default=StatusTicket.TU)

    class Meta:
        db_table = 'ticket'
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'


class SupportAnswer(models.Model):
    """ Support response """
    answer = models.TextField(verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')
    ticket = models.ForeignKey(
        Ticket, blank=True,
        null=True, related_name='support_answer',
        on_delete=models.CASCADE, verbose_name='Тикет')

    class Meta:
        db_table = 'support_answer'
        verbose_name = " Ответ саппорта"
        verbose_name_plural = " Ответы саппорта"

    def __str__(self):
        return f'{self.ticket}-{self.answer}'
