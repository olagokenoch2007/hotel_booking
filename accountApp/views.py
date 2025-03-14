from django.shortcuts import render, redirect, get_object_or_404
from .forms import Regform, BookingForms
from django.contrib.auth import login, authenticate, logout
from enochApp.models import *
from django.core.paginator import Paginator
# Create your views here.


def register(request):
    if request.method == "POST":
        register = Regform(request.POST)
        if register.is_valid():
            register.save()
            return redirect('accountApp:login')
    else:
        register= Regform()
    return render(request, "our_account/register.html", {'register':register})


def loginAcc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            return redirect('accountApp:dashboard')

    return render(request, "our_account/login.html")

def dashboard(request):
    apartment = Apartment.objects.all()
    return render(request, "our_account/dashboard.html", {"apartments": apartment})

def booking(request):
    bookings_list = Booking.objects.all()
    paginator = Paginator(bookings_list, 5)  # Show 5 bookings per page

    page_number = request.GET.get('page')  # Get the page number from the request
    bookings = paginator.get_page(page_number)  # Get the paginated page

    return render(request, "our_account/booking.html", {"bookings": bookings})

def logout_view(request):
    logout(request) 
    return redirect('accountApp:login')

def clientBooking(request):
    if request.method == 'POST':
        booking = BookingForms(request.POST)
        if booking.is_valid():
            booking.save()
            return redirect ('accountApp:booking')
    else:
        booking = BookingForms()
    return render (request, 'our_account/client_booking.html', {"booking": booking})


def editBooking(request, edit_id):
    single_booking = get_object_or_404(Booking, id=edit_id)
    if request.method == 'POST':
        booking = BookingForms(request.POST, instance=single_booking)
        if booking.is_valid():
            booking.save()
            return redirect('accountApp:booking')
        
    else:
        booking = BookingForms(instance=single_booking)
    return render(request, 'our_account/edit_booking.html', {"booking": booking})

def deleteBooking (request, delete_id):
    single_booking =  get_object_or_404(Booking, id=delete_id)
    single_booking.delete()
    return redirect('accountApp:booking')