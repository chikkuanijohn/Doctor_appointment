from django.urls import path
from . import views

urlpatterns=[
    path('',views.doctor_appointment_login),
    path('admin_home',views.admin_home),
    path('logout',views.doctor_appointment_logout),
    path('user_home',views.user_home),
    path('register/',views.register),
    path('booking/',views.booking_view),
    path('book_appointment/', views.book_appointment),  
    path('Contact/',views.Contact),
    path('view_bookings',views.view_bookings),
    path('add_details',views.add_details),
    path('check_up_packages/',views.check_up_packages),
    path('Manage/',views.Manage),
    path('Our_Team/',views.Our_Team),
    path('Testimonals/',views.Testimonals),
    path('booking',views.booking),
    path('booking_appoin',views.booking_appoin),
    path('view_doc',views.view_doc),
    path('edit_details/<pid>', views.edit_details),
    path('delete_details/<pid>', views.delete_details),

]                     