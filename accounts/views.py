from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from contacts.models import Contact
def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"successfully logined")
            return redirect('dashboard')
        else:
            messages.error(request,"invalid credentials")
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("fhjfj")
        messages.success(request,"logout successfully")
        return redirect('index')
    return redirect('index')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password != password2:
            messages.error(request,"Password is not matched")
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already used")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,\
                                             first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,"Registered successfully")
                    return redirect('login')

    else:
        return render(request, 'accounts/register.html')
def dashboard(request):
    contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #print(contacts)
    context={'contacts':contacts}
    return render(request, 'accounts/dashboard.html',context)
