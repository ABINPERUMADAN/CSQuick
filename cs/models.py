from secrets import choice
from cairo import Status
from django.db import models
from secretstorage import search_items

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30,null=False)
    username=models.CharField(primary_key=True,max_length=20,null=False)
    password=models.CharField(max_length=15,null=False)
    def __unicode__(self):
        return self.username
    
    def __str__(self):
        a=self.name
        b=self.username
        return (b)

class books(models.Model):
    
    bookid=models.CharField(max_length=20,null=False,primary_key=True)
    bookname=models.CharField(max_length=50,null=True)
    bookauthor=models.CharField(max_length=50,null=True)
    issuedate=models.DateField(null=True,blank=True)
    renewdate=models.DateField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True)
    user=models.ForeignKey(student,on_delete=models.SET_NULL,null=True,blank=True)
    status=models.IntegerField(default=3,null=False,help_text=('3->Nill','2->reserved,1->returned','0->not returned'),choices=((3,'Nill'),(2,'reserved'),(1,'retuned'),(0,'not returned')))
    
    def __unicode__(self):
        return self.bookid

    def __str__(self):
        return self.bookid+' '+self.bookname

# class studentlibrary(models.Model):
#     sbookid=models.ForeignKey(books,on_delete=models.DO_NOTHING,null=False,primary_key=True)
#     suser=models.ForeignKey(student,on_delete=models.DO_NOTHING,null=False)
#     issuedate=models.DateField()
#     returndate=models.DateField()
#     sStatus=models.IntegerField(default=0,null=False,help_text=('1->returned','0->not returned'),choices=((1,'retuned'),(0,'not returned')))
    
# class stafflibrary(models.Model):
#     stbookid=models.ForeignKey(books,on_delete=models.DO_NOTHING,null=False,primary_key=True)
#     stuser=models.ForeignKey(student,on_delete=models.DO_NOTHING,null=False)
#     issuedate=models.DateField()
#     returndate=models.DateField()
#     stStatus=models.IntegerField(default=0,null=False,help_text=('1->returned','0->not returned'),choices=((1,'retuned'),(0,'not returned')))
    

class laptop(models.Model):
    
    lapid=models.CharField(max_length=20,null=False,primary_key=True)
    datel=models.DateField(auto_now_add=True,null=False)
    user=models.ForeignKey(student,on_delete=models.SET_NULL,null=True, blank=True,default='')
    status=models.IntegerField(default=0,null=False,help_text=('2->not returned','1->returned'),choices=((0,'Nill'),(1,'retuned'),(2,'not returned')))
    
    def __str__(self):
        return self.lapid

class staff(models.Model):
    name=models.CharField(max_length=30,null=False)
    username=models.CharField(primary_key=True,max_length=20,null=False)
    password=models.CharField(max_length=15,null=False)
    def __unicode__(self):
        return self.username
    
    def __str__(self):
        a=self.name
        b=self.username
        return (b)

class events(models.Model):
    programme=models.CharField(max_length=20,null=True,blank=False)
    link=models.CharField(max_length=50,null=True,blank=False)
    by=models.CharField(max_length=20,null=True,blank=False)
    event_date=models.DateField(null=True,blank=False)
    photo=models.ImageField(null=True,blank=False)

    def __str__(self):
        return(self.programme)