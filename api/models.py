from django.db import models
from django.db.models.deletion import CASCADE

#Creating a custom user model to overide Django's default user model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name =self.name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Email & Password are required by default.

    def get_full_name(self):
        """required"""
        # The user is identified by their email
        return self.email

    def get_short_name(self):
        """required"""
        # The user is identified by their email
        return self.email

    def __str__(self):
        """required"""
        return self.email


class Contact(models.Model):
    """Class defines a contact object within the database"""
   
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


       
    
    


