from django.urls import path
from .views import SupportViewTicketsListStatus, SupportDetailTicketsAnswer, SupportMessageAnswer


urlpatterns = [
    path('status/<int:pk>', SupportViewTicketsListStatus.as_view(), name='support-view-ticket-list-status'),
    path('detail/<int:pk>', SupportDetailTicketsAnswer.as_view(), name='support-detail-ticket-answer'),
    path('message/<int:pk>', SupportMessageAnswer.as_view(), name='support-message-answer'),
    # path('support/detail/<int:pk>',)
]
