from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from support_system.serializers import SupportDetailTicketSerializer

from .models import Ticket


class DataMixinCustom(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SupportDetailTicketSerializer

    def get_queryset(self):
        try:
            id = self.kwargs['pk']
            queryset = Ticket.objects.get(id=id)
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
                queryset.status_ticket = serializer.validated_data['get_status_ticket_display']
                queryset.save()
                return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
