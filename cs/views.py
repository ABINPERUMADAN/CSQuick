

from os import uname
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
        j=0
        k=0
        for i in totlap:
            k+=1
        for i in totuser:
            if laptop.objects.filter(user=i.username):
                j+=1
        alap = k-j  
        if flag1=='1':
            userbooks=books.objects.filter(user=uname1).count
            book=books.objects.filter(user=uname1)

            a={'flag1':flag1,'uname':uname1,'totbooks':totbooks,'userbooks':userbooks,'book':book,
                    'totlaptop':totlaptop,'alap':alap,'logout':logout,'events':events_list}
            return render(request,'index.html',a)
        
        elif flag1=='2':
            userbooks=books.objects.filter(user=uname1).count
            book=books.objects.filter(user=uname1)
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
    a={'uname':uname1,'flag1':flag1}
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
    user=student.objects.get(username=uname1)
    book.status=2
    book.user=user
    book.save()
    return redirect('/searchbooks')

