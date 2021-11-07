from django.urls import path

from users.views import CreateUser, UserCreateTicket, UserQuestions, UserSeesDetailsTicket


urlpatterns = [
    path('register/', CreateUser.as_view()),
    path('all/', UserCreateTicket.as_view(), name='list-create-ticket'),
    path('detail/<int:pk>/', UserSeesDetailsTicket.as_view(), name='ticket-detail-view'),
    path('message/<int:pk>/', UserQuestions.as_view(), name='user-ask'),
]
