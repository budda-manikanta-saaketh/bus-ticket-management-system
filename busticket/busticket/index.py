from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from bticket.models import Ticket
from .forms import Booktickets,Ticketid_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_signup')
def home(request):
    return render(request,'home.html')
@login_required(login_url='login_signup')
def booktickets(request):
    tic_form=Booktickets()
    context={
        'form':tic_form
    }
    return render(request,'booktickets.html',context)
def login_signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login_signup.html')
def signup(request):
    if request.method=='POST':
        uname1=request.POST.get('username1')
        passw1=request.POST.get('password1')
        cpass=request.POST.get('cpassword')
        email=request.POST.get('email')
        pno=request.POST.get('phoneno')
        if passw1!=cpass:
            return HttpResponse("Your passwords does not match ")
        else:
            my_user=User.objects.create_user(uname1,email,passw1)
            my_user.save()
        return redirect('signup')
    return render(request,'signup.html')
@login_required(login_url='login_signup')
def viewtickets(request):
    ticid_form=Ticketid_form()
    context1={
        'form':ticid_form
    }
    return render(request,'viewtickets.html',context1)
def Logout(request):
    logout(request)
    return redirect('home')
def ticket_created(request):
    my_model=Ticket()
    if request.method=='POST':
        full_name=request.POST.get('Full_name')
        aad=request.POST.get('Aadhar_number')
        fro=request.POST.get('From')
        to=request.POST.get('To')
        date1=request.POST.get('date')
        no_of_seats=request.POST.get('Number_of_seats')
        price=150*int(no_of_seats)
        my_model=Ticket(full_name=full_name,aadhar_num=aad,From=fro,To=to,date=date1,no_of_seats=no_of_seats,price=price)
        my_model.save()
        ticket_id=my_model.id
        context={'ticket_id':ticket_id}
        return render(request,'ticket_created.html',context)
    tic_form = Booktickets()
    context = {'form': tic_form}
    return render(request, 'booktickets.html', context)
def ticket_list(request):
    if request.method=='POST':
        tid=request.POST.get('Ticket_Id')
    ticket= get_object_or_404(Ticket, id=tid)
    context = {'ticket': ticket}
    return render(request, 'tickets_list.html', context)