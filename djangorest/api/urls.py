from django.urls import path
from .views import UserRudView , UserAPIView


urlpatterns = [
    path( 'info',UserRudView.as_view(),name='user-rud'),
    path( 'gender',UserAPIView.as_view(),name='user-create'),
]
