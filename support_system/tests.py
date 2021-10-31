from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
import json

from support_system.models import Ticket


class SupportViewTicketsListStatusTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser('test name admin')

    def test_support_view_ticket_list_status(self):
        self.client.force_login(self.user)
        data = {"title": "Ticket 2",
                "content": "Text ticket 2",
                "status_ticket": "Тикет заморожен",
                "user": self.user
                }
        url = reverse('support-view-ticket-list-status', kwargs={'pk': self.user.id})
        response = self.client.get(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.client.logout()
        response = self.client.get(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)


class SupportMessageAnswerTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser('super user admin')
        self.ticket = Ticket.objects.create(
            title="Test task 1",
            content="Test text tack 1",
            status_ticket="Тикет решен",
            user=self.user
        )

    def test_support_message_answer(self):
        self.client.force_login(self.user)
        url = reverse('support-message-answer', kwargs={'pk': self.user.id})
        data = {'title': 'Test task 1',
                'content': 'Test text tack 1',
                'status_ticket': 'Тикет решен',
                'user': self.user.id
                }
        response = self.client.get(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['status_ticket'], data['status_ticket'])
        ticket = Ticket.objects.get(**data)
        self.assertEqual(response.data['user'][list(response.data['user'])[0]], ticket.user.id)
       # ticket = self.ticket = Ticket.objects.create(status_ticket="Тикет решен", user_id=self.user.id)
       # response = self.client.put(url, data=ticket, content_type='application/json')
       # self.assertEqual(response.status_code, status.HTTP_200_OK)
