from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Attendee
from .forms import EventForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Case, When, Value, IntegerField


# STAFF ACCESS VIEWS

@staff_member_required
def event_list(request):
    events = Event.objects.all()
    events = Event.objects.order_by(
        Case(
            When(is_published=True, then=Value(0)),
            default=Value(1),
            output_field=IntegerField(),
        ),
        'date'
    )
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
    events = Event.objects.filter(is_published=True).order_by('date')

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
    booked_events = Attendee.objects.filter(user=request.user).values_list('event', flat=True)
    events = Event.objects.filter(id__in=booked_events)
    return render(request, 'event/booked_list.html', {'events': events})


def book_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        
        quantity = int(request.POST.get('quantity', 1))

        for _ in range(quantity):
            Attendee.objects.create(user=request.user, event=event)

        return redirect('event_public_detail', event_id=event.id)
    
    return redirect('event_public_detail', event_id=event_id)

# CANCELLING BOOKING

@login_required
def perform_cancel_booking(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    booking = Attendee.objects.filter(user=request.user, event=event).first()

    if booking:
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'Booking not found.')

    return redirect('booked_list')


def toggle_event_visibility(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        # Toggle the is_hidden status
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