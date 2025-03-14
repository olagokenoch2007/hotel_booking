from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import BookingForms

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.

def myHome(request):
    get_rooms = Apartment.objects.all()[ :3]
    return render(request, "index.html", {'get_all_rooms': get_rooms})

def myAbout(request):
    return render(request, "about.html")

def myBook(request, room_id):
    details = get_object_or_404(Apartment, id=room_id)

    if request.method == "POST":
        book = BookingForms(request.POST)
        if book.is_valid():
            book.save()
            myName = book.cleaned_data ["name"]
            myEmail = book.cleaned_data["email"]
            checkin = book.cleaned_data["check_in"]
            checkout = book.cleaned_data["check_out"]
            room = book.cleaned_data["room"]
            mail_subject = "Confirmation Of Booking"
            mail_content = {
                "name" : myName,
                "email" : myEmail,
                "checkin" : checkin,
                "checkout" : checkout,
                "room" : room,
            }


            html_message =  render_to_string ("email_template.html", mail_content)
            plain_text = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [myEmail]

            try:
                email_message = EmailMessage(mail_subject, plain_text, from_email, recipient_list)
                email_message.send()
                messages.success(request, "Booking confirmation email sent successfully")
            except Exception as e:
                messages.error(request, f"Failed to send confirmation email: {e}")

    else:
        book = BookingForms()

    return render(request, "booking.html", {"details": details, "book_us": book})


def Booking(request):
    book = BookingForms()
    return render(request, "booking.html", {'book_us': book})


def myContact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Contact message sent successfully")
             
    return render(request, "contact.html")

def myRoom(request):
    get_hotel = Apartment.objects.all()[: 6]
    return render(request, "room.html", {'hotel': get_hotel})

def myService(request):
    return render(request, "service.html")

def myTeam(request):
    staff = Staff.objects.all()
    return render(request, "team.html", {'staff_members': staff})

def myTestimonial(request):
    return render(request, "testimonial.html")

def roomDetails(request, room_id):
    details = get_object_or_404(Apartment, id=room_id)
    return render(request, "single-room-detail.html", {"details" : details})