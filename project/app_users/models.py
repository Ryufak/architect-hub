from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from main.utilities import simple_uuid

class CustomUserManager(BaseUserManager):

    #If you have any other REQUIRED_FIELDS, be sure to put them in as callable arguments
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("This field is required!")
        if not username:
            raise ValueError("This field is required")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.is_active      = True
        user.is_validated   = True
        
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser):

    # These are required
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    # Activation and Validation
    activation_key      = models.CharField(default=simple_uuid, max_length=36)
    is_validated        = models.BooleanField(default=False)
    
    # Other
    COUNTRY = (
        ('Bulgaria', 'Bulgaria'), 
        ('USA', 'USA'), 
        ('Russia', 'Russia'), 
        ('Vatican', 'The Vatican'))

    first_name          = models.TextField(max_length=20, verbose_name='First name')
    last_name           = models.TextField(max_length=20, verbose_name='Last name')
    country             = models.CharField(max_length=20, choices=COUNTRY, default=COUNTRY[0])
    city                = models.TextField(max_length=30)
    about               = models.CharField(max_length=600)
    certification       = models.URLField()




    USERNAME_FIELD = 'email'
    #Lists which fields are required when creating a user
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    #Displays returned value when you print a CustomUser object
    def __str__(self):
        return self.username

    #Required functions
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    



