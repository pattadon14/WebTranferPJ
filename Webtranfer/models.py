from django.db import connections
from django.db import models

# Create your models here.
class College(models.Model):
    C_name = models.CharField(max_length=200,null=False,unique=True)

    class Meta:
        db_table ="College"   
        ordering = ('id',) 

    def __str__(self):
        return self.C_name
    
class Coll_Major(models.Model):
    Cmj_name = models.CharField(max_length=200,null=False,unique=False)
    Coll_name = models.ForeignKey(College,on_delete=models.CASCADE)
    

    class Meta:
        db_table ="Coll_Majors"
        ordering = ('id',)
        unique_together = ('Cmj_name', 'Coll_name',)

    def __str__(self):
        return self.Cmj_name
    
    def __unicode__(self):
        return self.Coll_name.Coll_name

class Faculty(models.Model):
    Fac_Name = models.CharField(max_length=200,null=False,unique=True)

    class Meta:
        db_table ="Faculty"
        ordering = ('id',)

    def __str__(self):
        return self.Fac_Name


class Major(models.Model):
    Mj_Name = models.CharField(max_length=200,null=False,unique=True)
    Fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    class Meta:
        db_table ="Major"
        ordering = ('id',)

    def __str__(self):
        return self.Mj_Name
    
    def __unicode__(self):
        return self.Fac_name.Fac_name
    
class Groups(models.Model):
    G_Name = models.CharField(max_length=200,null=False,unique=True,)
    Mj_Name = models.ForeignKey(Major,on_delete=models.CASCADE,related_name='Major')
    Fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='Faculty')

    class Meta:
        db_table ="Groups"
        ordering = ('id',)    
   
    def __str__(self):
        return self.G_Name
    
class User(models.Model):
    Username = models.CharField(max_length=50,null=False,unique=True)
    Password = models.CharField(max_length=50,null=False,unique=True)
    

    class Meta:
        db_table ="User"
        ordering = ('id',) 

    def __str__(self):
        return self.Username
    
class Advisor(models.Model):
    Adv_Fname = models.CharField(max_length=255,null=False,unique=False)
    Adv_Lname = models.CharField(max_length=255,null=False,unique=False)
    Fac_Name = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    Mj_Name = models.ForeignKey(Major,on_delete=models.CASCADE)
    Username = models.CharField(max_length=50,null=False,unique=True)
    Password = models.CharField(max_length=50,null=False,unique=True)

    class Meta:
        db_table ="Advisor"
        ordering = ('id',)    

    def __str__(self):
        return self.Adv_Fname

class Student(models.Model):
    Std_ID = models.IntegerField(primary_key=True,null=False,unique=True)
    Std_Fname = models.CharField(max_length=255,null=False,unique=False)
    Std_Lname = models.CharField(max_length=255,null=False,unique=False)
    Stdusername = models.ForeignKey(User,on_delete=models.CASCADE)
    Mj_Name = models.ForeignKey(Major,on_delete=models.CASCADE)
    G_Name = models.ForeignKey(Groups,on_delete=models.CASCADE)
    #Year
    Adv_Name = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    Cmj_Name = models.ForeignKey(Coll_Major,on_delete=models.CASCADE)

    class Meta:
        db_table ="Student"
        ordering = ('Std_ID',)    

class Cur_Group(models.Model):
    CG_Name = models.CharField(max_length=255,null=False,unique=False)

    class Meta:
        db_table ="Cur_Group"
        ordering = ('id',) 

    def __str__(self):
        return self.CG_Name
    
class Cur_Head(models.Model):
    Mj_Name = models.ForeignKey(Major,on_delete=models.CASCADE)
    Ac_Year = models.DateField((""), auto_now=False, auto_now_add=False)
    Version = models.CharField(max_length=255,null=False,unique=False)
    Cr_total = models.IntegerField((""),null=False)
    Cr_Man = models.IntegerField((""),null=False)
    Cr_Math = models.IntegerField((""),null=False)
    Cr_Lang= models.IntegerField((""),null=False)
    Cr_Core = models.IntegerField((""),null=False)
    Cr_Basic = models.IntegerField((""),null=False)
    Cr_Main = models.IntegerField((""),null=False)
    Cr_Select = models.IntegerField((""),null=False)
    Cr_Free= models.IntegerField((""),null=False)

    class Meta:
        db_table ="Cur_Head"
        ordering = ('id',)   

class Cur_Detail(models.Model):
    Cur_Name =  models.ForeignKey(Cur_Head,on_delete=models.CASCADE) 
    CG_Name = models.ForeignKey(Cur_Group,on_delete=models.CASCADE)
    Subj_ID =  models.IntegerField(primary_key=True,null=False,unique=True)
    Subj_Cr = models.IntegerField((""),null=False)
    
    class Meta:
        ordering = ('Subj_ID',) 

class Useradmin(models.Model):
    Adm_Fname = models.CharField(max_length=255,null=False,unique=False)
    Adm_Lname = models.CharField(max_length=255,null=False,unique=False)
    Username = models.CharField(max_length=50,null=False,unique=True)
    Password = models.CharField(max_length=50,null=False,unique=True)
    

    class Meta:
        db_table ="Admin"
        ordering = ('id',) 

    def __str__(self):
        return self.Username 
    