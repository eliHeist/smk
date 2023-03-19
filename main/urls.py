from django.urls import path

from main.views import landingPageView

app_name = 'main'

urlpatterns = [
    path('', landingPageView, name='landingpage')
]