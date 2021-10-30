from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from support_system.models import Ticket


class ListCreateTicketTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('test name')

    def test_list_create_ticket(self):
        self.client.force_login(self.user)
        data = {
            'title': 'test title',
            'content': 'test test content',
            'user': self.user.id
        }
        url = reverse('list-create-ticket')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        # self.assertEqual(response.data['support_answer'], data['support_answer'])
        ticket = Ticket.objects.get(**data)
        self.assertEqual(response.data['id'], ticket.id)

    def test_ticket_detail(self):
        self.client.force_login(self.user)
        data = {
            'title': 'test title',
            'content': 'test test content',
            'status_ticket': 'Тикет не решен',
            # 'user': self.user.id,
        }
        url = reverse('list-create-ticket')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['status_ticket'], data['status_ticket'])
    # ticket = Ticket.objects.get(**data)
    # self.assertEqual(response.data['id'], ticket.id)
