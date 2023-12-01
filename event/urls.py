from django.urls import path
from .views import event_list, event_detail, create_event, register_event, event_edit, event_delete

urlpatterns = [
    path('', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/create/', create_event, name='create_event'),
    path('events/<int:event_id>/edit/', event_edit, name='event_edit'),
    path('events/<int:event_id>/register/', register_event, name='register_event'),
    path('events/<int:event_id>/delete/', event_delete, name='event_delete'),
    # ... other paths ...
]