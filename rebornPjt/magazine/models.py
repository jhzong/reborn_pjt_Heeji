from django.db import models

# Create your models here.

class Magazine_code(models.Model):
    mtype = models.CharField(max_length=2)
    mtype_desc = models.CharField(max_length=100)
    mdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.mtype},{self.mtype_desc}'
    

class Magazine(models.Model):
    mno = models.AutoField(primary_key=True)
    mtitle = models.CharField(max_length=1000)
    mcontent = models.TextField()
    magazine_code = models.ForeignKey(Magazine_code,on_delete=models.SET_NULL,null=True)
    mfile = models.FileField(default='',null=True,blank=True)
    mhit = models.IntegerField(default=0)
    mdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.mno},{self.mtitle}'
    

