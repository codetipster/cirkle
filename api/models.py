from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Contact(models.Model):
    """Class defines a contact object within the database"""

    # RELATIONSHIP = (
    #     ("Friend", "a friend"),
    #     ("Family", "met as family"),
    #     ("Office", "met at the office"),
    #     ("Stranger", "A stranger")

    # )
   
    name = models.CharField(max_length=40,  blank=False, unique=False) 
    phone_number = models.CharField(max_length=14, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    address = models.TextField(max_length=200, unique=False, blank=True)
    #Every contact has a relationship for the user based on the choice listings
    # relation = models.CharField(max_length=50, blank=False, choices= RELATIONSHIP)
    created_on = models.DateTimeField( null=True, auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)


    #Specify how Django should convert this contact object to human readable form at the admin interface
    def __str__(self):
        return self.name


       
    
    


