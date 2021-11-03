from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from support_system.models import SupportAnswer, Ticket
from support_system.serializers import SupportAnswerSerializer, SupportSerializer
from support_system.utils import DataMixinCustom


class SupportViewTicketsListStatus(ListAPIView):
    """
    Support видит решенные, нерешенные и замороженные тикеты
    Используемые endpoints:
    api/support_system/status/<id> (id: 1-'тикет заморожен'; 2-'тикет не решен'; 3 -'тикет не решен')
    api/support_system/detail/<id> - Детальная иформация по конкретному тикету ( по его id), возможность поменять статус
    api/support_system/message/<id> -Support может написать пользователю ответ на его тикет ( id - тикет)

    """

    serializer_class = SupportSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        if self.kwargs['pk'] not in range(1, 4):
            raise Http404
        return Ticket.objects.filter(status_ticket=self.kwargs['pk']).order_by('-updated_at')


class SupportDetailTicketsAnswer(DataMixinCustom):
    """
    Support видит детальную информацию тикета (по его id) и может поменять статус
    Используемые endpoints:
    api/support_system/status/<id> (id: 1-'тикет заморожен'; 2-'тикет не решен'; 3 -'тикет не решен')
    api/support_system/detail/<id> - Детальная иформация по конкретному тикету ( по его id), возможность поменять статус
    api/support_system/message/<id> -Support может написать пользователю ответ на его тикет ( id - тикет)

    """


class SupportMessageAnswer(DataMixinCustom):
    """
    Support может написать пользователю ответ по выбраному тикету (по его id):
    Используемые endpoints:
    api/support_system/status/<id> (id: 1-'тикет заморожен'; 2-'тикет не решен'; 3 -'тикет не решен')
    api/support_system/detail/<id> - Детальная иформация по конкретному тикету ( по его id), возможность поменять статус
    api/support_system/message/<id> -Support может написать пользователю ответ на его тикет ( id - тикет)

    """

    serializer_class = SupportAnswerSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            queryset, id = self.get_queryset()
            if serializer.is_valid(raise_exception=True) and id:
                SupportAnswer.objects.create(ticket_id=id, answer=serializer.validated_data['support_answer'])
                return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
