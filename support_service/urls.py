from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/support_system/', include('support_system.urls')),
    path('api/user/', include('users.urls')),
]
