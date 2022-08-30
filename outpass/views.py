from django.views import generic
from django.core.mail import send_mail,EmailMultiAlternatives
from .forms import OutpassForm
from django.shortcuts import render,reverse,redirect
from django.template import loader
from datetime import date,datetime, timedelta



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
            if context['name']=='1':
                context.update({
                    'name':'Siva Prakash K',
                    'roll_number':'19BCS073',
                    'email':'sivaprakash.19cs@kct.ac.in',
                })
                
            subject=f"Outing Request Approved- {context['name']} {context['roll_number']}"
            from_email='Hostel KCT'
            recipient_list=[context['email'],]
            html_message = loader.render_to_string('outpass_body.html', context)

            send_mail(
                subject=subject,
                message='',
                from_email=from_email,
                recipient_list=recipient_list,
                html_message=html_message
            )
            return redirect(reverse('home'))
    context={
        'form':form
    }
    return render(request,'outpass_form.html',context)