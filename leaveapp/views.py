from pickle import GET
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect,HttpResponse
from.models import Login,Register,Leaveapply,Leaveapprove,Leavereject,Leavedetails

def home(request):
    return render(request,'aelog.html')

def emp(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'LOGGED IN SUCCESSFULLY')
            return render(request,'aelog.html')
        else:
            messages.info(request,'ENTER CREDENTIALS')
            return render(request,'aelog.html')
    else:
        return render(request,'login.html')

def ad(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        if username == 'admin' and password == 'admin':
            messages.success(request, 'LOGGED IN SUCCESSFULLY')
            return render(request,'admindash.html')
        else:
            messages.success(request, 'INVALID')
            return render(request,'aelog.html')

def employee(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        if username == 'emp' and password == 'emp':
            messages.success(request, 'LOGGED IN SUCCESSFULLY')
            return render(request, 'user.html')
        else:
            messages.success(request, 'INVALID')
            return render(request, 'aelog.html')

def empleave(request):
    if request.method == 'POST':
        userid = request.user.id 
        name = request.POST['name']
        startingdate = request.POST['startingdate']
        endingdate = request.POST['endingdate']
        reason = request.POST['reason']
        Leavedetails(userid=userid, name=name, startingdate=startingdate, endingdate=endingdate,
                     reason=reason, status="pending").save()
        messages.info(request,'YOUR LEAVE REQUEST HAS BEEN SUBMITTED')
        return render (request,"leaveapply.html")
    else:
        return render (request,"leaveapply.html")

def leavedetails(request):
        x = Leavedetails.objects.all()
        return render(request,'leavedetails.html', {'all':x})
# function for approve button in leave details.html
def leaveedit(request,i):
    e = Leavedetails.objects.filter(id=i)
    return render (request,'leaveapprove.html',{'all': e})
# function for reject button in leavedetails.html
def leaveedit1(request,i):
    e = Leavedetails.objects.filter(id=i)
    return render(request, 'leavereject.html', {'all': e})

# function for approve button in leaveapprove.html
def leaveapprove(request,i):
    if request.method == 'POST':
        x = Leavedetails.objects.get(id=i)
        x.name = request.POST['name']
        x.startingdate = request.POST['startingdate']
        x.endingdate = request.POST['endingdate']
        x.reason = request.POST['reason']
        x.status = "Approved"
        x.save()
        messages.info(request,"LEAVE HAS BEEN APPROVED")
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})
    else:
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})
# function for reject button in leavereject.html

def leavereject(request,i):
    if request.method == 'POST':
        x = Leavedetails.objects.get(id=i)
        x.name = request.POST['name']
        x.startingdate = request.POST['startingdate']
        x.endingdate = request.POST['endingdate']
        x.reason = request.POST['reason']
        x.status = "Rejected"
        x.save()
        messages.info(request,"LEAVE HAS BEEN REJECTED")
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})
    else:
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})
# function for employee to view his own leave status

def leavestatus(request):
    userid = request.user.id
    x = Leavedetails.objects.filter(userid=userid)
    return render(request, 'leavestatus.html', {'all': x})

