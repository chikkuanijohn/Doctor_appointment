from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User

# Create your views here.

def doctor_appointment_login(req):
        if 'admin' in req.session:
            return redirect(admin_home)
        if 'user' in req.session:
            return redirect(user_home)
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
        
                    req.session['admin']=uname 
                    return redirect(admin_home)
                else:
                    req.session['user']=uname 
                    return redirect(user_home)
            else:
                messages.warning(req,'invalid username or password')
                return redirect(doctor_appointment_login)  
        else:
            return render(req,'login.html')

def doctor_appointment_logout(req):
    logout(req)
    req.session.flush() 
    return redirect(doctor_appointment_login)
#--------------------admin----------------------
def admin_home(req):
    
    if 'admin' in req.session:
        data=Doctor.objects.all()
    
        return render(req,'admin/home.html',{'Doctor':data})
    else:
       return redirect(doctor_appointment_login)
    
def user_home  (req)  :
    return render(req,'user/user_home.html')

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req,'invalid username or password')
            return redirect(register)   
        return redirect(doctor_appointment_login) 
    else:
        return render(req,'user/register.html') 
    


def booking_view(request):
    return render(request, 'booking.html') 
   
def book_appointment(request):
    return render(request, 'booking/book_appointment.html') 

 
def Contact(request):
    return render(request, 'Contact.html')