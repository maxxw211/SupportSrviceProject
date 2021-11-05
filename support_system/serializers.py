from rest_framework import serializers

from users.serializers import UserAskSerializer, UserSerializers, AnswerForUserSerializers

from .models import Ticket


class SupportSerializer(serializers.ModelSerializer):
    """
    use: >>> class SupportViewTicketsListStatus():

    """
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers()
    # support_answer = AnswerForUserSerializers(many=True, read_only=True)
    user_ask = UserAskSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'content', 'status_ticket', 'user', 'user_ask']


class SupportMsgSerializer(serializers.ModelSerializer):
    """"""
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    user = UserSerializers(read_only=True)
    user_ask = UserAskSerializer(many=True, read_only=True)
    support_answer = serializers.CharField(max_length=255, write_only=True, style={'base_template': 'textarea.html'})

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')


class SupportDetailSerializer(serializers.ModelSerializer):
    status_ticket = serializers.ChoiceField(choices=Ticket.StatusTicket.choices, source='get_status_ticket_display')
    user = UserSerializers(read_only=True)
    support_answer = AnswerForUserSerializers(many=True, read_only=True)
    user_ask = UserAskSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'status_ticket', 'user', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')
