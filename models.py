from django.db import models
import datetime

# Create your models here.
User_Gender = ('Female', 'Female'), ('Male', 'Male')
Blood_Type = ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), (
    'O-', 'O-')


class user(models.Model):
    FName = models.CharField(max_length=30, verbose_name='Your First Name')
    MName = models.CharField(max_length=30, verbose_name='Your Middle Name')
    LName = models.CharField(max_length=30, verbose_name='Your Last Name')
    Mail = models.EmailField(verbose_name='Your Email')
    Number = models.IntegerField(verbose_name='Your Phone Number')
    Add = models.CharField(max_length=40, verbose_name='Your Address')
    gen = models.CharField(verbose_name='Gender', choices=User_Gender, default='Female')


class dietician(user):
    Exp = models.IntegerField(verbose_name='Experience', help_text='Years of your experience')


class treatement(models.Model):
    Date = models.DateField()
    Description = models.CharField(max_length=40)
    dietitian = models.ForeignKey(dietician, verbose_name='Dietician Info', on_delete=models.CASCADE)


class patient(user):
    Blood = models.CharField(max_length=4, verbose_name='Your Blood type', choices=Blood_Type, default=None)
    Age = models.IntegerField(help_text='Your Age')
    doc = models.ForeignKey(dietician, verbose_name='Dietician informations', related_name='diet',
                            on_delete=models.CASCADE)
    treat = models.ForeignKey(treatement, verbose_name='Treatment details', related_name='treatement',
                              on_delete=models.CASCADE)



class appointment(models.Model):
    Created_At = models.DateTimeField(auto_now=True)
    diet = models.ForeignKey(dietician, related_name='dietician', on_delete=models.CASCADE,
                             verbose_name='Dietician informations' nombre telephone="474777")



class invoice(models.Model):
    Date_Invoice = models.DateField(verbose_name='Invoice Date')
    Amount = models.FloatField()
    app = models.OneToOneField(appointment, verbose_name='Appointment info', on_delete=models.PROTECT)
