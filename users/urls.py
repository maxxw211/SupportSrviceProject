from django.urls import path

from users.views import ListCreateTicket, TicketDetailView, UserAsk

urlpatterns = [
    path('all/', ListCreateTicket.as_view(), name='list-create-ticket'),
    path('detail/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail-view'),
    path('message/<int:pk>/', UserAsk.as_view(), name='user-ask'),
]
