from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    #If you have any other REQUIRED_FIELDS, be sure to put them in as callable arguments
    def create_user(self, email, username, password=None):
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
        
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    #These are required
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    #Custom fields go here


    #Sets what field is required to log in (default is username)
    USERNAME_FIELD = 'email'
    #Lists which fields are required when creating a user
    REQUIRED_FIELDS = ['username',]
    #Referencing the Manager
    objects = CustomUserManager

    #Displays returned value when you print a CustomUser object
    def __str__(self):
        return self.username

    #Required functions
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perm(self, app_label):
        return True



