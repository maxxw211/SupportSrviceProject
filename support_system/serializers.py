from rest_framework import serializers
from .models import Ticket, SupportAnswer
from users.serializers import UserAskSerializers, UserSerializers


class SupportAnswerSerializers(serializers.ModelSerializer):
    """ Ответ Суппорта use:>>> TicketSerializer >>> SupportSerializer >>> UserAskSerializer"""

    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = SupportAnswer
        fields = ['id', 'answer', 'created_at']


class TicketSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    support_answer = SupportAnswerSerializers(many=True, read_only=True)
    user_ask = UserAskSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'status_ticket', 'support_answer', 'user_ask']


class SupportSerializer(serializers.ModelSerializer):
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers()
    support_answer = SupportAnswerSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'content', 'status_ticket', 'user', 'support_answer']


class SupportAnswerSerializer(serializers.ModelSerializer):
    """"""
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers(read_only=True)
    user_ask = UserAskSerializers(many=True, read_only=True)
    support_answer = serializers.CharField(max_length=255, write_only=True, style={'base_template': 'textarea.html'})

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')


class SupportDetailSerializer(serializers.ModelSerializer):
    status_ticket = serializers.ChoiceField(choices=Ticket.StatusTicket.choices, source='get_status_ticket_display')
    user = UserSerializers(read_only=True)
    support_answer = SupportAnswerSerializers(many=True, read_only=True)
    user_ask = UserAskSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')
