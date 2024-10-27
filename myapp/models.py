from django.db import models
from ckeditor.fields import RichTextField
class person(models.Model):
	first_name=models.CharField(max_length=1000)
	last_name=models.CharField(max_length=1000)
	def __str__(self):
		return self.first_name

class article(models.Model):
    name=models.CharField(max_length=100)
    title=models.TextField(max_length=1000,blank=True)
    image=models.ImageField(upload_to="data",blank=True)
    writer=models.CharField(max_length=50)
    date=models.CharField(max_length=100)
    content=models.TextField(blank=True)
    link=models.URLField(max_length=1000)
    video=models.FileField(upload_to="data", blank=True)
    def __str__(self):
    	return self.name
class myreview(models.Model):
    Title=models.CharField(max_length=100)  
    message=models.TextField(max_length=1000)
    def __str__(self):
    	return self.Title
class myhelp(models.Model):
    Title=models.CharField(max_length=100)  
    message=models.TextField(max_length=1000)
    def __str__(self):
    	return self.Title
class mycontact(models.Model):
    Name=models.CharField(max_length=100)  
    Email=models.CharField(max_length=100)
    Subject=models.CharField(max_length=1000)
    Message=models.TextField(max_length=1000)
    def __str__(self):
    	return self.Name
class userregister(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname =models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    CPassword=models.CharField(max_length=100)
    Contact=models.CharField(max_length=100,blank=True,null=True)
    Gender=models.CharField(max_length=100,blank=True,null=True)
    Age=models.CharField(max_length=100,blank=True,null=True)
    Address=models.CharField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.Firstname
class universities(models.Model):
    Name=models.CharField(max_length=100)
    Ranking=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    EstablishedYear=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    Enrollment=models.CharField(max_length=100,blank=True)
    link=models.URLField(max_length=1000, blank=True)
    Image=models.ImageField(upload_to='data',blank=True)
    def __str__(self):
        return self.Name
class courses(models.Model):
    coursename=models.CharField(max_length=1000)
    ctype=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return self.coursename
class countries(models.Model):
    Countryname=models.CharField(max_length=100,primary_key=True)
    Image=models.ImageField(upload_to='data',blank=True)
    def __str__(self):
         return self.Countryname

class cun_details(models.Model):
    Countryname=models.ForeignKey(countries, on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='data',blank=True)
    heading=models.CharField(max_length=100,primary_key=True)
    des=RichTextField()
class visa(models.Model):
    Countryvisa=models.ForeignKey(countries, on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='data',blank=True)
    heading=models.CharField(max_length=100,primary_key=True)
    des=RichTextField()
class video(models.Model):
    Title=models.TextField()
    Video=models.FileField(upload_to="data",blank=True)
    def __str__(self):
        return self.Title

