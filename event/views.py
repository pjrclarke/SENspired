from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Attendee
from .forms import EventForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

# STAFF ACCESS VIEWS

@staff_member_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})

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
        form = EventForm(request.POST, request.FILES, instance=event)
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

@login_required
def event_book(request):
    events = Event.objects.all()
    return render(request, 'event/event_book.html', {'events': events})

@login_required
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

def booked_list(request):
    # Fetch the events that the user has booked
    booked_events = Attendee.objects.filter(user=request.user).values_list('event', flat=True)
    events = Event.objects.filter(id__in=booked_events)
    return render(request, 'event/booked_list.html', {'events': events})


def book_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        # Check if the user is already booked for this event
        if not Attendee.objects.filter(user=request.user, event=event).exists():
            # Book the event for the user
            Attendee.objects.create(user=request.user, event=event)
            # Redirect to a success page or event detail page
            return redirect('event_public_detail', event_id=event.id)
        else:
            # Redirect to a page indicating that the user is already booked
            return redirect('event_public_detail', event_id=event.id)

    # Handle the case where the user accesses the page without a POST request
    # (e.g., directly accessing the URL)
    return redirect('event_public_detail', event_id=event_id)

# CANCELLING BOOKING

@login_required
def perform_cancel_booking(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        # Check if the user has booked this event
        booking = Attendee.objects.filter(user=request.user, event=event).first()

        if booking:
            # Delete the booking for the user and event
            booking.delete()
            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        else:
            # Return a JSON response indicating that the user hasn't booked this event
            return JsonResponse({'success': False, 'message': 'You have not booked this event.'})
    else:
        # Return a JSON response indicating an error for non-POST requests
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})