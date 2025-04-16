from django.db import models

# Create your models here.


class Contact(models.Model):
    """  """

    GRADE = (
        ('5',"5-sinf"),
        ('6',"6-sinf"),
        ('7',"7-sinf"),
        ('8',"8-sinf"),
        ('9',"9-sinf"),
    )

    full_name = models.CharField(max_length=50, verbose_name="Ism familiya")
    school = models.CharField(max_length=255, verbose_name="Maktab")
    grade = models.CharField(max_length=50, choices=GRADE ,verbose_name="Sinf") # sinf
    phone_number = models.CharField(max_length=13, verbose_name="Tel. raqam")
    
    created_on = models.DateTimeField(auto_now_add=True) # vaqtni o'zi aftomatik oladi








