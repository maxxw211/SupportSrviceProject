from django.contrib.auth.models import User
from rest_framework import serializers
from support_system.models import Ticket, SupportAnswer
from users.models import UserAsks


class AnswerForUserSerializers(serializers.ModelSerializer):
    """ Ответ Суппорта use: >>> UserAskSerializer"""

    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = SupportAnswer
        fields = ['id', 'answer', 'created_at']


class UserAskSerializers(serializers.ModelSerializer):
    """ Вопрос Юзера use: >>> TicketSerializer >>> SupportDetailSerializer """
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = UserAsks
        fields = ['id', 'answer', 'created_at']


class UserSerializers(serializers.ModelSerializer):
    """  Описание Юзера use: >>> SupportSerializer >>> SupportDetailSerializer"""

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class UserAskSerializer(serializers.ModelSerializer):
    """ Serializer юзер задает вопрос api/user/message/id/ """

    user_ask = serializers.CharField(max_length=255, write_only=True, style={'base_template': 'textarea.html'})
    support_answer = AnswerForUserSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')
