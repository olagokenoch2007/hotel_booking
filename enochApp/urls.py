from django.urls import path
from enochApp import views

app_name = 'enochApp'

urlpatterns = [
    path('', views.myHome, name='home'),
    path('about/', views.myAbout, name='about'),
    path('booking/<str:room_id>/', views.myBook, name='booking_detail'),  # For booking a specific room
    path('contact/', views.myContact, name='contact'),
    path('room/', views.myRoom, name='room'),
    path('service/', views.myService, name='service'),
    path('team/', views.myTeam, name='team'),
    path('testimonial/', views.myTestimonial, name='testimonial'),
    path('roomdetails/<str:room_id>/', views.roomDetails, name='details'),
    path('booking/', views.Booking, name='booking_list'),  # For general booking page
]