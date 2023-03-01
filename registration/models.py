from django.db import models
# from .models import *
#--------------------[ Teacher Database ]-------------------#
class Teacher(models.Model):
    t_id = models.AutoField(primary_key = True)
    t_name = models.CharField(max_length=50,null=False)
    t_email = models.EmailField(max_length=254)
    t_password = models.CharField(max_length = 100)
    t_profile = models.ImageField(upload_to = 'teacher/')

    def __str__(self):
        return self.t_name


#--------------------[ Student Database ]-------------------#
class Student(models.Model):
    s_id = models.AutoField(primary_key = True)
    s_name = models.CharField(max_length=50)
    s_email = models.EmailField(max_length=254)
    s_password = models.CharField(max_length = 100)
    s_profile = models.ImageField(upload_to = 'student/')
    def __str__(self):
        return self.s_name
    

    #s_name, s_email, s_password