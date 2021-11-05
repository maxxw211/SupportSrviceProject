from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from support_system.models import Ticket

from users.models import UserAsks

from users.serializers import UserAskSerializer, TicketSerializer, UserRegisterSerializer


class CreateUserView(ListCreateAPIView):
    """
    Создаем Пользователя
    Используемые endpoints:
    api/user/register/ - Регистрация пользователя
    api/user/all/ - Текущий пользователь видит все свои тикеты
    api/user/detail/1/ - Детальная информация по конкретному тикету ( по его id)
    api/user/message/1/ -Пользователь пишет доп. вопрос по тикету (по его id)
    """

    model = User
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class ListCreateTicket(ListCreateAPIView):
    """ Пользователь пишет тикет и отправляет его, а так же он может видеть все свои тикеты
    и всю информацию связанную с ними.
    Используемые endpoints:
    api/user/all/ - Текущий пользователь видит все свои тикеты
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user).order_by('-support_answer__created_at').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketDetailView(ListAPIView):
    """ Пользователь может просматривать историю тикета
    Используемые endpoints:
    api/user/detail/1/ - Детальная иформация по каждому отдельно взятому тикету ( по id тикета)
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user, id=self.kwargs['pk'])


class UserAsk(ListCreateAPIView):
    """ Сообщение пользователя
    Используемые endpoints:
    api/user/message/1/ -Пользователь может написать доп. вопрос по тикету (по его id)
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = UserAskSerializer

    def get_queryset(self):
        try:
            id = self.kwargs['pk']
            queryset = Ticket.objects.filter(user_id=self.request.user.pk).get(id=id)
            return queryset, id
        except Ticket.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        try:
            queryset, id = self.get_queryset()
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            queryset, id = self.get_queryset()
            if serializer.is_valid(raise_exception=True) and id:
                UserAsks.objects.create(ticket_id=id, answer=serializer.validated_data['user_ask'])

                return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
