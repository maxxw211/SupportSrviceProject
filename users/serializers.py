from django.contrib.auth.models import User

from rest_framework import serializers

from support_system.models import SupportResponse, Ticket

from users.models import UserQuestion


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ["id", "username", "password", ]


class ResponseToUserSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = SupportResponse
        fields = ['id', 'answer', 'created_at']


class UserQuestionSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = UserQuestion
        fields = ['id', 'answer', 'created_at']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class UserAskQuestionSerializer(serializers.ModelSerializer):
    user_ask = serializers.CharField(max_length=255, write_only=True, style={'base_template': 'textarea.html'})
    support_answer = ResponseToUserSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'support_answer', 'user_ask']
        read_only_fields = ('title', 'content')


class TicketSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)
    update_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)
    status_ticket = serializers.CharField(source='get_status_ticket_display', read_only=True)
    support_answer = ResponseToUserSerializers(many=True, read_only=True)
    user_ask = UserQuestionSerializers(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'content', 'created_at', 'update_at', 'status_ticket', 'support_answer', 'user_ask']
