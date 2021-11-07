from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from support_system.models import SupportResponse, Ticket
from support_system.serializers import SupportMsgSerializer, SupportSerializer
from support_system.utils import DataMixinCustom


class SupportSeesStatusTickets(ListAPIView):
    """ Саппорт видит статус тикета по его  api/support_system/status/<id>
    (id: 1-'тикет заморожен'; 2-'тикет решен'; 3 -'тикет не решен')
    """

    serializer_class = SupportSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        if self.kwargs['pk'] not in range(1, 4):
            raise Http404
        return Ticket.objects.filter(status_ticket=self.kwargs['pk']).order_by('-updated_at')


class SupportSeesDetailInfoTicketsResponse(DataMixinCustom):
    """
    Саппорт видит всю информацию по каждому тикету пользователя (по id тикета) и имеет возможность изменять статус
    api/support_system/detail/<id>
    """


class SupportResponseMessage(DataMixinCustom):
    """ Саппорт имеет возможность дать ответ пользователю  api/support_system/message/<id> (по id тикета) """

    serializer_class = SupportMsgSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            queryset, sup_resp_id = self.get_queryset()
            if serializer.is_valid(raise_exception=True) and sup_resp_id:
                SupportResponse.objects.create(
                    ticket_id=sup_resp_id,
                    answer=serializer.validated_data['support_answer']
                )
                return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
