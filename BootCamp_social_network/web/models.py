from django.db import models
# from django_jalali.db import models as jmodels
from model_utils import Choices
from multiselectfield import MultiSelectField
# Create your models here.


class Userss(models.Model):
    domains_of_speciality = (
        ('pure javascript front end' , 'JS'),
        ('query javascript front end' , 'JQuery'),
        ('angular javascript front end' , 'Angular JS'),
        ('html' , 'HTML'),
        ('css' , 'CSS'),
        ('javascript back end' , 'Node.JS'),
        ('C-bsaed' , 'C/C++'),
        ('desktop C' , 'C#'),
        ('objective C' , 'Objective C'),
        ('JAVA SE' , 'JAVA SE')
    )

    domains_of_interests = (
        ('BACKEND web development' , 'BACKEND'),
        ('FRONTEND web development' , 'FRONTEND'),
        ('desktop apps' , 'DESKTOP APPLICATIONS'),
        ('android apps' , 'ANDROID APPLICATIONS'),
        ('ios apps' , 'IOS APPLICATIONS'),
        ('network apps' , 'NETWORK APPLICATIONS'),
        ('security' , 'SECURITY')
    )
    Camper_Name_Firstname = models.CharField(max_length = 20 , blank = False , null = False , unique = True , default = '')
    Camper_Name_Lastname = models.CharField(max_length = 20 , blank = False , null = False , unique = True , default = '')
    Password = models.CharField(max_length = 10 , blank = False , null = False)
    Age = models.IntegerField()
    Years_Of_Exprience = models.IntegerField()
    Programming_Languages = MultiSelectField(choices = domains_of_speciality, blank = True , null = True)
    Interests = MultiSelectField(choices = domains_of_interests, blank = True , null = True)
    Personal_Image = models.ImageField(blank = True , null = True , upload_to = "personal_image/%Y/%M/%D/")


class Job_opportunity(models.Model):
    domains_of_speciality = (
        ('pure javascript front end' , 'JS'),
        ('query javascript front end' , 'JQuery'),
        ('angular javascript front end' , 'Angular JS'),
        ('html' , 'HTML'),
        ('css' , 'CSS'),
        ('javascript back end' , 'Node.JS'),
        ('C-bsaed' , 'C/C++'),
        ('desktop C' , 'C#'),
        ('objective C' , 'Objective C'),
        ('JAVA SE' , 'JAVA SE')
    )
    Company_Name = models.CharField(max_length = 20 , blank = False , null = False , default = '')
    
