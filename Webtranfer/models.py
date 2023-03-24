from django.db import connections
from django.db import models

# Create your models here.
class College(models.Model):
    C_name = models.CharField(max_length=200,null=False,unique=True)

    class Meta:
        db_table ="College"    

    def __str__(self):
        return self.C_name
    
class Coll_Major(models.Model):
    Cmj_name = models.CharField(max_length=200,null=False,unique=False)
    Coll_name = models.ForeignKey(College,on_delete=models.CASCADE)
    

    class Meta:
        db_table ="Coll_Majors"

    def __str__(self):
        return self.Cmj_name
    
class Faculty(models.Model):
    Fac_Name = models.CharField(max_length=200,null=False,unique=True)

    class Meta:
        db_table ="Faculty"

    def __str__(self):
        return self.Fac_Name
    
class Major(models.Model):
    Mj_Name = models.CharField(max_length=200,null=False,unique=True)
    Fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    class Meta:
        db_table ="Major"

    def __str__(self):
        return self.Mj_Name
    
class Groups(models.Model):
    G_Name = models.CharField(max_length=200,null=False,unique=True,)
    Mj_Name = models.ForeignKey(Major,on_delete=models.CASCADE,related_name='Major')
    Fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='Faculty')

    class Meta:
        db_table ="Groups"    
   
    def __str__(self):
        return self.G_Name

class UserType(models.Model):
    UT_ID = models.IntegerField(primary_key=True,null=False,unique=True)
    UT_Name = models.CharField(max_length=50,null=False,unique=True)

    class Meta:
        db_table ="UserType"  

    def __str__(self):
        return self.UT_ID
    
class User(models.Model):
    Username = models.CharField(max_length=50,null=False,unique=True)
    Password = models.CharField(max_length=50,null=False,unique=True)
    UT_ID = models.ForeignKey(UserType,on_delete=models.CASCADE)

    class Meta:
        db_table ="User"  

    def __str__(self):
        return self.Username
    
    