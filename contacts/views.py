from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
def contacts(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        user_id=request.POST['user_id']
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        title=request.POST['listing']
        message=request.POST['message']
        realtor_email=request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"you have already made a enquiry for  this lisitng")
                print("ug3wfbjefbjefjbefkj")
                return redirect('/listings/'+listing_id)
        contact = Contact(listing_id=listing_id, user_id=user_id, email=email, name=name, phone=phone, listing=title,
                          message=message)
        contact.save()
        from django.core.mail import send_mail
        send_mail(
            'BTM Realtor State Inquiry details',
            'Thank you for contacting us, we will back you soon',
            'kumarhimanshu901@gmail.com',
            ['kumarhimanshu901@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,"successfully enquiry submitted")
        return redirect('/listings/'+listing_id)
    #return render(request,'/listings/')


