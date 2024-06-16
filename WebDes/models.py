from django.db import models
from AuthReg.models import User
# Create your models here.
class Customers(models.Model):
    First_name=models.CharField(max_length=255, blank=False)
    Last_name=models.CharField(max_length=255, blank=False)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255, null=False)
    document=models.CharField(max_length=255, null=False)
    budget=models.FloatField()
    User_ID = models.ForeignKey(User, to_field='id', on_delete=models.PROTECT)

    def __str__(self):
        return self.First_name
class Provider(models.Model):
    Company_name=models.CharField(max_length=255, null=False)
    materials=models.CharField(max_length=255, null=False, unique=True)
    tech=models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.Company_name
class Contractor(models.Model):
    name=models.CharField(max_length=255, null=False)
    price=models.FloatField()
    workers=models.IntegerField(unique=True)
    User_ID = models.ForeignKey(User, to_field='id', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
class Employees(models.Model):
    Designer=models.IntegerField()
    Builders=models.IntegerField()
    Arcitectors=models.IntegerField()
    Electrications=models.IntegerField()

    def __str__(self):
        return ('Employees')
class Projects(models.Model):
    Project_name=models.CharField(max_length=255, null=False)
    Customers=models.ForeignKey(Customers, on_delete=models.PROTECT)
    Geo_info=models.CharField(max_length=255, null=False)
    materials=models.ForeignKey(Provider, to_field='materials',
                                related_name='materials_article_set', on_delete=models.PROTECT)
    obur=models.ForeignKey(Provider, to_field='tech',
                           related_name='obur_article_set', on_delete=models.PROTECT)
    My_workers=models.ForeignKey(Employees, on_delete=models.PROTECT)
    Given_workers=models.ForeignKey(Contractor, to_field='workers', on_delete=models.PROTECT)
    Status=models.BooleanField
    User_ID = models.ForeignKey(User, to_field='id', on_delete=models.PROTECT)

    def __str__(self):
        return self.Project_name
class   zayavka(models.Model):
    first_name=models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    phone= models.IntegerField(null=False)
    ur_lico= models.BooleanField(default=False)
    work_type=models.CharField(max_length=255, null=False)
    User_ID = models.ForeignKey(User, to_field='id', on_delete=models.PROTECT, null=True)
    Commentary = models.CharField(max_length=255)
    Date=models.DateField(auto_now=True)
    Status=models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)
    Deleted_Date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.first_name

class main_tovar(models.Model):
    name=models.CharField(max_length=255, null=False)
    ploshad = models.CharField(max_length=255, null=False)
    cost = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to="static/img",height_field=None, width_field=None, null=True, blank=True)
    def __str__(self):
        return self.name


