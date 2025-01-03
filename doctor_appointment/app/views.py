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
    
    
def user_home(req):
     if 'user' in req.session:
         data=Doctor.objects.all()
         return render(req,'user/user_home.html',{'Doctor':data})
     else:
          return redirect(doctor_appointment_login)
    
    
       





def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        print(uname,email,pswd)
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
    return render(request,'booking.html') 
   
def book_appointment(request):
            if request.method=='POST':
                name=request.POST['name']
                email=request.POST['email']
                date=request.POST['date']
                message=request.POST['message']
                print(name,email,date,message)
                try:
                   data=User.objects.create_user(name=name,email=email,date=date,message=message)
                   data.save()
                except:
                     messages.warning(request,'invalid email')
                     return redirect(book_appointment) 
                return redirect(user_home) 
            else:  
  
                return render(request,'user/book_appointment.html')


 
def Contact(request):
    return render(request,'Contact.html')


def check_up_packages(request):
    return render(request,'check_up_packages.html')

def Manage(request):
    return render(request,'Manage.html')

def Our_Team(request):
    return render(request,'Our_Team.html')

def Testimonals(request):
    return render(request,'Testimonals.html')

def booking(request):
    return render(request,'booking.html')




def view_bookings(request):
    # buy=Buy.objects.all()[::-1]
    return render(request,'admin/view_bookings.html')

def view_doc(request):
    return render(request,'view_doc.html')


def add_details(req):

    if 'admin' in req.session:
        if req.method == 'POST':
           
            name = req.POST['name']
            specialty = req.POST['specialty']
             
            available_days = req.POST['available_days']
            available_time_start = req.POST['available_time_start']
            available_time_end= req.POST['available_time_end']
            # file = req.FILES['img']

            data = Doctor.objects.create(
                 name=name, specialty=specialty,  available_days= available_days,
                available_time_start=available_time_start,available_time_end=available_time_end)
               
            data.save()
            return redirect(admin_home)
        else:
            return render(req, 'admin/add_details.html')
    else:
        return redirect(doctor_appointment_login)
    

def edit_details(req, pid):
    if 'admin' in req.session:
        if req.method == 'POST':
            name = req.POST['name']
            specialty = req.POST['specialty']
            available_days = req.POST['available_days']
            available_time_start = req.POST['available_time_start']
            available_time_end = req.POST['available_time_end']
            # file = req.FILES.get('img')  
            # if file:
            #     Doctor.objects.filter(pk=pid).update(name=name,specialty=specialty,available_days=available_days, available_time_start= available_time_start,available_time_end =available_time_end)
            #     data=Doctor.objects.get(pk=pid)
            #     data.img=file
            #     data.save()
            # else:  
            Doctor.objects.filter(pk=pid).update(name=name,specialty=specialty,available_days=available_days, available_time_start= available_time_start,available_time_end =available_time_end)
            data=Doctor.objects.get(pk=pid)
            data.save()
            return redirect(admin_home)
        else:
            data=Doctor.objects.get(pk=pid)
            return render(req,'admin/edit.html',{'data':data})

def delete_details(req,pid):
    data=Doctor.objects.get(pk=pid)
    # file=data.img.url
    # file=file.split('/')[-1]
    # os.remove('media/'+file)
    data.delete()
    return redirect(admin_home)