from django.urls import path
from accountApp import views


app_name = 'accountApp'


    
urlpatterns = [
   path('register/', views.register, name = 'register'),
   path('login/', views.loginAcc, name = 'login'),
   path('dashboard/', views.dashboard, name = 'dashboard'),
   path('booking/', views.booking, name = 'booking'),
   path('logout/', views.logout_view, name='logout'),
   path('client-booking/', views.clientBooking, name='bookclient'),
   path('edit-booking/<str:edit_id>/', views.editBooking, name='bookedit'),
   path('delete-booking/<str:delete_id>/', views.deleteBooking, name='delete'),
]
