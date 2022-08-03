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

class laptop(models.Model):
    
    lapid=models.CharField(max_length=20,null=False,primary_key=True)
    renew_date=models.DateField(null=True,blank=False)
    student_user=models.ForeignKey(student,on_delete=models.SET_NULL,null=True, blank=True,default='')
    staff_user=models.ForeignKey(staff,on_delete=models.SET_NULL,null=True, blank=True,default='')
    status=models.IntegerField(default=0,null=False,help_text=('3->reserved','2->not returned','1->returned','0->Nill'),choices=((0,'Nill'),(1,'retuned'),(2,'not returned'),(3,'reserved')))
    
    def __str__(self):
        return self.lapid

class books(models.Model):
    
    bookid=models.CharField(max_length=20,null=False,primary_key=True)
    bookname=models.CharField(max_length=50,null=True)
    bookauthor=models.CharField(max_length=50,null=True)
    issuedate=models.DateField(null=True,blank=True)
    renewdate=models.DateField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True)
    student_user=models.ForeignKey(student,on_delete=models.SET_NULL,null=True,blank=True)
    staff_user=models.ForeignKey(staff,on_delete=models.SET_NULL,null=True,blank=True)
    status=models.IntegerField(default=3,null=False,help_text=('3->Nill','2->reserved,1->returned','0->not returned'),choices=((3,'Nill'),(2,'reserved'),(1,'retuned'),(0,'not returned')))
    
    def __unicode__(self):
        return self.bookid

    def __str__(self):
        return self.bookid+' '+self.bookname

class events(models.Model):
    programme=models.CharField(max_length=20,null=True,blank=False)
    link=models.CharField(max_length=50,null=True,blank=False)
    by=models.CharField(max_length=20,null=True,blank=False)
    event_date=models.DateField(null=True,blank=False)
    photo=models.ImageField(null=True,blank=False)

    def __str__(self):
        return(self.programme)