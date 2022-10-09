from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    start_date=models.DateField(null=True , blank=True)
    end_date=models.DateField(null=True ,blank=True)


    def __str__(self) -> str:
        return self.email

    