import email
import time
from unicodedata import name
from xmlrpc.client import Boolean
from django.views import generic
from django.core.mail import send_mail,EmailMessage
from .forms import OutpassForm
from django.shortcuts import render,reverse,redirect
from django.template import loader
from datetime import date,datetime, timedelta
# from students.models import User
from outpass import settings
# import pytz

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
                'time':(datetime.now()+timedelta(hours=+5,minutes=+30)).strftime("%I:%M %p")
                
            }
            if context['name']=='1':
                Student_name="Siva Prakash K"
                Student_email="sivaprakash.19cs@kct.ac.in"
                Student_roll="19BCS073"
            Student_name=context['name']
            Student_email=context['email']
            Student_roll=context['roll_number']
            validDomain=Student_email[-9:]=='kct.ac.in'
            if Student_name=="1":
                Student_email="sivaprakash.19cs@kct.ac.in"
                Student_roll="19BCS073"
            
            # if(Student_name.isnumeric()):
            #     if not shortExists(Student_name):
            #         return render(request,'outpass_form.html',{'alert_msg':'you have no shortcuts please enter full details','form':OutpassForm()})
            #     else :
            #         student=getStudentByShort(Student_name)

            # else:
            #     if  emailExists(Student_email):
            #         student=getStudentByEmail(Student_email)
            #     else:
            #         if validDomain:
            #             student=createStudent(Student_name,Student_email,Student_roll,'')
                    
            # if ((not Student_name.isnumeric()) and (not validDomain)):
            #         return render(request,'outpass_form.html',{'alert_msg':'only valid email','form':OutpassForm()})

                
            # student.clicks+=1
            # student.save()
            # Student_name=student.name
            # Student_email=student.email
            # Student_roll=student.roll_number

            
            # if not student.isAllowed:
            #     subject="Fake Pass"
            #     from_email='Aavin temple'
            #     html_message = loader.render_to_string('outpass_reject_body.html', context)
            # else:
            # context.update({
            #         'name':Student_name
            #     })
            subject=f"Outing Request Approved- {Student_name} {Student_roll}"
            from_email='Hostel KCT'
            html_message = loader.render_to_string('outpass_body.html', context)
                
                
            recipient_list=[Student_email,]
            
            print(subject,recipient_list,html_message)

            if not settings.ENVIRONMENT:
                # send_mail(
                #     subject=subject,
                #     message='',
                #     from_email=from_email,
                #     recipient_list=recipient_list,
                    
                #     html_message=html_message
                # )
                print("send_mail success")
                email=EmailMessage(
                    subject=subject,
                    body=html_message,
                    from_email=from_email,
                    to=recipient_list,
                    cc=['hostelkctt@outlook.com','securittyoffficer@outlook.com'],
                    
                )
                email.content_subtype="html"
                email.send()
                print("EmailMessage success")
                time.sleep(2)
            return render(request,'outpass_form.html',{'alert_msg':'Pass sent','form':OutpassForm()})
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