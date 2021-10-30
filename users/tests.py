from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
import json
from support_system.models import Ticket


class ListCreateTicketTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('test name')

    def test_list_create_ticket(self):
        self.client.force_login(self.user)
        data = {
            'title': 'test title',
            'content': 'test test content',
            'user': self.user.id,
        }
        url = reverse('list-create-ticket')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        ticket = Ticket.objects.get(**data)
        self.assertEqual(response.data['id'], ticket.id)

    def test_ticket_detail_view(self):
        self.client.force_login(self.user)
        data = {
            'content': 'test test content',
            'status_ticket': 'Тикет не решен',
            'support_answer': [],
            'user_ask': [],
            'user': self.user.id,
        }
        url = reverse('list-create-ticket')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['status_ticket'], data['status_ticket'])
        self.assertEqual(response.data['support_answer'], data['support_answer'])
        self.assertEqual(response.data['user_ask'], data['user_ask'])
        data.pop('content')
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.client.logout()
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)
