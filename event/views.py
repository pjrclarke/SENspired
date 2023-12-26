from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Attendee, Booking
from .forms import EventForm, BookingForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone



# STAFF ACCESS VIEWS

@staff_member_required
def event_list(request):
    events = Event.objects.all().order_by(
        Case(
            When(is_published=True, then=Value(0)),
            default=Value(1),
            output_field=IntegerField(),
        ),
        'date'
    )

    # Filter out rejected bookings
    bookings = Booking.objects.exclude(status='rejected')

    return render(request, 'event/event_list.html', {'events': events, 'bookings': bookings})

@staff_member_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendees = Attendee.objects.filter(event=event)
    remaining_capacity = event.max_capacity - attendees.count()

    return render(
        request,
        'event/event_detail.html',
        {'event': event, 'attendees': attendees, 'remaining_capacity': remaining_capacity}
    )

@staff_member_required
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'event/event_form.html', {'form': form})

@staff_member_required
@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id, organizer=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, 'event/event_edit.html', {'form': form, 'event': event})

@staff_member_required
@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id, organizer=request.user)

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('event_list')

    return redirect('event_list')

@staff_member_required
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Attendee.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event.id)

# USER ACCESS VIEWS


def event_book(request):
    current_date = timezone.now().date()
    events = Event.objects.filter(is_published=True, date__gte=current_date).order_by('date')
    
    return render(request, 'event/event_book.html', {'events': events})


def event_public_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    return render(request,
        'event/event_public_detail.html',
        {'event': event}
    )


def home(request):
    return render(request, 'event/index.html')

# 404
def custom_404(request, exception):
    return render(request, 'event/404.html', status=404)

# USER BOOKED EVENTS

@login_required
def booked_list(request):
    booked_events = Attendee.objects.filter(user=request.user).values_list('event', flat=True)
    events = Event.objects.filter(id__in=booked_events)
    bookings = Booking.objects.filter(user=request.user).order_by('date')
    return render(request, 'event/booked_list.html', {'events': events, 'bookings': bookings})


@login_required
def book_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        
        quantity = int(request.POST.get('quantity', 1))

        for _ in range(quantity):
            # Create multiple Attendee instances
            Attendee.objects.create(user=request.user, event=event)

        messages.success(request, f'Successfully booked {quantity} tickets for the event.')
        return redirect('event_public_detail', event_id=event.id)
    
    return redirect('event_public_detail', event_id=event_id)


# CANCELLING BOOKING FOR USER

# @login_required
# def delete_booking(request, event_id):
#     # Get the event instance
#     event = get_object_or_404(Attendee, user=request.user, pk=event_id)

#     # Get the booking instance for the authenticated user and the specified event
#     booking = Attendee.objects.filter(user=request.user, pk=event_id).first()

#     if booking:
#         if request.method == 'POST':
#             # Delete both the booking and the event
#             booking.delete()
#             event.delete()
#             return redirect('booked_list')
#     else:
#         # Handle the case where the booking is not found
#         messages.error(request, 'Booking not found.')

#     return render(request, 'event/booking_confirm_delete.html', {'booking': booking, 'event': event})

@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.filter(id=booking_id)
    if request.method == 'GET':
        booking.delete()
        return redirect('booked_list')
    return render(request, 'event/booking_confirm_delete.html', {'booking': booking})


@login_required
def cancel_event(request, event_id):
    event = Event.objects.filter(id=event_id)
    if request.method == 'GET':
        event.delete()
        return redirect('booked_list')
    return render(request, 'event/booking_confirm_delete.html', {'event': event})


# TOGGLING EVENT VISIBILITY FOR USER

# @login_required
# def delete_booking(request, event_id):
#     booking = Attendee.objects.filter(user=request.user, pk=event_id).first()
    
#     print(booking)


def toggle_event_visibility(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        event.is_published = not event.is_published
        event.save()

    return redirect('event_list')

# ACCOUNT OVERVIEW

@login_required
def account_overview(request):
    return render(request, 'event/account_overview.html')



@login_required
def account_edit(request):
    user_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'event/account_edit.html', {'user_data': user_data})

@login_required
def perform_edit_account(request):
    if request.method == 'POST':

        if 'profile_image' in request.FILES:
            request.user.profile_image = request.FILES['profile_image']

        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.username = request.POST.get('username', '')
        request.user.email = request.POST.get('email', '')

        request.user.save()

        return redirect('account_overview')  

    user_data = {
        'first_name': request.user.first_name or '',
        'last_name': request.user.last_name or '',
        'username': request.user.username,
        'email': request.user.email,
    }

    return render(request, 'event/account_edit.html', {'user_data': user_data})


def coming_soon(request):
    return render(request, 'event/coming_soon.html')

# BOOKING SPACE FOR USERS

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    print(bookings)  # Add this line to print the bookings to the console
    return render(request, 'event/event_list.html', {'bookings': bookings})

@login_required
def booking_request(request):
    bookings = Booking.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking_request = form.save(commit=False)
            booking_request.user = request.user
            booking_request.save()
            return redirect('booked_list') 
    else:
        form = BookingForm()

    return render(request, 'event/booking_form.html', {'form': form, 'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booked_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'event/booking_form_edit.html', {'form': form})



@staff_member_required
@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Add logic to update the booking status to 'approved'
    booking.status = 'approved'
    booking.save()

    # Redirect back to the booking list or any other appropriate page
    return redirect('event_list')

@staff_member_required
@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Add logic to update the booking status to 'rejected'
    booking.status = 'rejected'
    booking.save()

    # Redirect back to the booking list or any other appropriate page
    return redirect('booked_list')
