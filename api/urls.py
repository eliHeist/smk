from django.urls import path

from api.views import notificationView, salesApiView

app_name = 'api'

urlpatterns = [
    path('sales/', salesApiView, name='sales'),
    path('notifications/', notificationView, name='notifications'),
]