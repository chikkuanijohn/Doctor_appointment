from django.urls import path
from . import views

urlpatterns=[
    path('',views.doctor_appointment_login),
    path('admin_home',views.admin_home),
    path('logout',views.doctor_appointment_logout),
    path('user_home',views.user_home),
    path('register/',views.register),
    path('booking/',views.booking_view),
   path('booking/book_appointment/', views.book_appointment),  
]                     