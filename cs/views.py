

import os
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from requests import post
# Create your views here.


# global uname1,flag1

def home(request):
    return render(request,'home.html')

def signin(request):
    global flag1
    global uname1
    flag1=0
    if request.method=='POST':
        uname1=request.POST['username']
        pass1=request.POST['password']
        
        if student.objects.filter(username=uname1).filter(password=pass1):
            flag1='1'
            
            return redirect('main',uname1)
        
        elif staff.objects.filter(username=uname1).filter(password=pass1):
            flag1='2'
            flag=1
            return redirect('main',uname1)
    return render(request,'signin.html')

def main(request,uname1):
    if flag1!=0:
        totbooks=books.objects.all().count

        totlaptop=laptop.objects.all().count
        totuser=student.objects.all()
        totlap=laptop.objects.all()
        events_list=events.objects.all()
        
        
        alap =laptop.objects.filter(status=0).count()
        if flag1=='1':
            userbooks=books.objects.filter(student_user=uname1).count
            book=books.objects.filter(student_user=uname1)

            a={'flag1':flag1,'uname':uname1,'totbooks':totbooks,'userbooks':userbooks,'book':book,
                    'totlaptop':totlaptop,'alap':alap,'logout':logout,'events':events_list}
            return render(request,'index.html',a)
        
        elif flag1=='2':
            userbooks=books.objects.filter(staff_user=uname1).count
            book=books.objects.filter(staff_user=uname1)
            a={'flag1':flag1,'uname':uname1,'totbooks':totbooks,'userbooks':userbooks,'book':book,
                    'totlaptop':totlaptop,'alap':alap,'logout':logout,'events':events_list}
            return render(request,'index.html',a)
        else:
            flag1==0
    else:
        
        return render(request,'index.html',{'flag1':flag1})


def logout(request):
    flag1=0
    return redirect('/sign')

def library1(request):
    a={'uname':uname1,'flag1':flag1}
    return render(request,'library.html',a)

def laptop1(request):
    if flag1=='1':       
        ulap=laptop.objects.filter(student_user=uname1).count()
        lap=laptop.objects.filter(student_user=uname1).first()
    else:
        ulap=laptop.objects.filter(staff_user=uname1).count()
        lap=laptop.objects.filter(staff_user=uname1).first()

    alap =laptop.objects.filter(status=0).count()
    
    a={'uname':uname1,'flag1':flag1,'alap':alap,'ulap':ulap,'lap':lap}
    return render(request,'laptop.html',a)

def searchbooks(request):
    if request.method=='POST':
        searched=request.POST['search']
        name=books.objects.filter(bookname__contains=searched)
        # status=books.objects.filter(bookname__contains=searched)
        a={'searched':searched,
            'name':name,'uname':uname1,'flag1':flag1}

        return render(request,'searched.html',a)
    else:
        return render(request,'searched.html',{'flag1':flag1})

def book_status(request,bookname):
    book=books.objects.get(bookname=bookname)
    if flag1=='1':
        user=student.objects.get(username=uname1)
        book.student_user=user
    else:
        user=staff.objects.get(username=uname1)
        book.staff_user=user
    book.status=2
    
    book.save()
    return redirect('/searchbooks')

def laptop_status(request):
    lap=laptop.objects.filter(status=0).first()
    if flag1=='1':
        user=student.objects.get(username=uname1)
        lap.student_user=user
    else:
        user=staff.objects.get(username=uname1)
        lap.staff_user=user
    lap.status=3
    
    lap.save()
    return redirect('/laptop')