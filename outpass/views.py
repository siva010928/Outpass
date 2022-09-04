import email
import time
from unicodedata import name
from xmlrpc.client import Boolean
from django.views import generic
from django.core.mail import send_mail
from .forms import OutpassForm
from django.shortcuts import render,reverse,redirect
from django.template import loader
from datetime import date,datetime, timedelta
from students.models import User
from outpass import settings
 

def outpass_form_view(request):
    form=OutpassForm()
    if request.method=="POST":
        form=OutpassForm(request.POST)
        if form.is_valid():

            
            context={
                'name':form.cleaned_data['name'],
                'roll_number':form.cleaned_data['roll_number'],
                'email':form.cleaned_data['email'],
                'date':date.today().strftime("%Y-%m-%d"),
                'time':(datetime.now()+timedelta(minutes=-5)).strftime("%I:%M %p")
                
            }
            
            Student_name=context['name']
            Student_email=context['email']
            Student_roll=context['roll_number']
            
            if(Student_name.isnumeric()):
                if not shortExists(Student_name):
                    return render(request,'outpass_form.html',{'no_short':True,'form':OutpassForm()})
                else :
                    student=getStudentByShort(Student_name)
            else:
                if  emailExists(Student_email):
                    student=getStudentByEmail(Student_email)
                else:
                    student=createStudent(Student_name,Student_email,Student_roll,'')
                
            student.clicks+=1
            student.save()
            Student_name=student.name
            Student_email=student.email
            Student_roll=student.roll_number

            
            if not student.isAllowed:
                subject="Fake Pass"
                from_email='Aavin temple'
                html_message = loader.render_to_string('outpass_reject_body.html', context)
            else:
                context.update({
                    'name':Student_name
                })
                subject=f"Outing Request Approved- {Student_name} {Student_roll}"
                from_email='Hostel KCT'
                html_message = loader.render_to_string('outpass_body.html', context)
                
                
            recipient_list=[Student_email,]
            
            print(subject,recipient_list,html_message)

            if not settings.DEBUG:
                send_mail(
                    subject=subject,
                    message='',
                    from_email=from_email,
                    recipient_list=recipient_list,
                    html_message=html_message
                )
            time.sleep(2)
            return render(request,'outpass_form.html',{'pass':True,'form':OutpassForm()})
    context={
        'form':form
    }
    return render(request,'outpass_form.html',context)

def emailExists(email)->Boolean:
    if  User.objects.filter(email=email).exists():
        return True
    return False


def shortExists(name)->Boolean:
     if User.objects.filter(short=name).exists():
         return True
     return False
 
def  getStudentByShort(name):
    return User.objects.get(short=name)

def  getStudentByEmail(email):
    return User.objects.get(email=email)

def createStudent(name,email,roll_number,short):
    return User.objects.create(name=name,
                                                email=email,
                                                roll_number=roll_number,
                                                short=short)