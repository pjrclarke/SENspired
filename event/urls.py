from django.urls import path
from .views import event_list, event_detail, create_event, register_event, event_edit, event_delete, event_book, home, event_public_detail, booked_list, book_event, perform_cancel_booking, account_overview, account_edit, perform_edit_account, coming_soon, toggle_event_visibility

urlpatterns = [
    path('', home, name='home'),
    path('events/edit_listings', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/create/', create_event, name='create_event'),
    path('events/<int:event_id>/edit/', event_edit, name='event_edit'),
    path('events/<int:event_id>/register/', register_event, name='register_event'),
    path('events/<int:event_id>/delete/', event_delete, name='event_delete'),
    path('events/book', event_book, name='event_book'),
    path('events/detail/<int:event_id>', event_public_detail, name='event_public_detail'),
    path('events/booked_list', booked_list, name='booked_list'),
    path('events/detail/<int:event_id>', event_public_detail, name='event_public_detail'),
    path('events/<int:event_id>/book/', book_event, name='book_event'),
    path('events/<int:event_id>/cancel_booking/', perform_cancel_booking, name='perform_cancel_booking'),
    path('events/account_overview/', account_overview, name='account_overview'),
    path('events/account_edit/', account_edit, name='account_edit'),
    path('perform_edit_account/', perform_edit_account, name='perform_edit_account'),
    path('coming_soon/', coming_soon, name='coming_soon'),
    path('toggle_event_visibility/<int:event_id>/', toggle_event_visibility, name='toggle_event_visibility'),


]