from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from support_system.models import Ticket

from users.models import UserQuestion

from users.serializers import UserAskQuestionSerializer, TicketSerializer, UserRegisterSerializer


class CreateUser(ListCreateAPIView):
    """ api/user/register/ - Пользователь регистрируется """

    model = User
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserCreateTicket(ListCreateAPIView):
    """ api/user/all/ - Пользователь пищет тикет, отправляет, а так же видит все свои тикеты """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user).order_by('-support_answer__created_at').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSeesDetailsTicket(ListAPIView):
    """ api/user/detail/1/ - Видит всю информацию по каждому конкретному тикету ( по id тикета) """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user, id=self.kwargs['pk'])


class UserQuestions(ListCreateAPIView):
    """ api/user/message/1/ - Может задать доп. вопрос по тикету (по id тикета) """

    permission_classes = [IsAuthenticated, ]
    serializer_class = UserAskQuestionSerializer

    def get_queryset(self):
        try:
            ticket_pk = self.kwargs['pk']
            queryset = Ticket.objects.filter(user_id=self.request.user.pk).get(id=ticket_pk)
            return queryset, ticket_pk
        except Ticket.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        try:
            queryset, ticket_pk = self.get_queryset()
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            queryset, ticket_pk = self.get_queryset()
            if serializer.is_valid(raise_exception=True) and ticket_pk:
                UserQuestion.objects.create(ticket_id=ticket_pk, answer=serializer.validated_data['user_ask'])

                return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
