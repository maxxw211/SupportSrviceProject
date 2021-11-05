from django.urls import path

from .views import SupportSeesDetailInfoTicketsResponse, SupportResponseMessage, SupportSeesStatusTickets

urlpatterns = [
    path('status/<int:pk>', SupportSeesStatusTickets.as_view(), name='support-view-ticket-list-status'),
    path('detail/<int:pk>', SupportSeesDetailInfoTicketsResponse.as_view(), name='support-detail-ticket-answer'),
    path('message/<int:pk>', SupportResponseMessage.as_view(), name='support-message-answer'),
    # path('support/detail/<int:pk>',)
]
