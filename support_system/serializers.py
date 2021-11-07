from rest_framework import serializers

from users.serializers import ResponseToUserSerializers, UserAskQuestionSerializer, UserSerializers

from .models import Ticket


class SupportSerializer(serializers.ModelSerializer):
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers()
    user_ask = UserAskQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'content', 'status_ticket', 'user', 'user_ask']


class SupportMsgSerializer(serializers.ModelSerializer):
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers(read_only=True)
    user_ask = UserAskQuestionSerializer(many=True, read_only=True)
    support_answer = serializers.CharField(max_length=255, write_only=True, style={'base_template': 'textarea.html'})

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')


class SupportSeesDetailTicketSerializer(serializers.ModelSerializer):
    status_ticket = serializers.ChoiceField(choices=Ticket.StatusTicket.choices, source='get_status_ticket_display')
    user = UserSerializers(read_only=True)
    support_answer = ResponseToUserSerializers(many=True, read_only=True)
    user_ask = UserAskQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')
