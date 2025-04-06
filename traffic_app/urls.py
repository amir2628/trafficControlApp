from django.urls import path
from .views import control_dashboard, update_state

urlpatterns = [
    path('', control_dashboard, name='control_dashboard'),
    path('update-state/', update_state, name='update_state'),
]
