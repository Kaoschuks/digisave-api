from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import date
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class MyUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True


    def create_user(self, email, phone, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """ 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        print(user)
        return
        if not email:
            raise ValueError(_('The Email must be set'))
        elif not phone:
            raise ValueError(_('The phone number is already registered with an account'))
        else:
            user.save()
            return user

    # python manage.py createsuperuser
    def create_superuser(self, email, phone, is_staff, password):
        user = self.model(
                          email = email,  
                          phone = phone,                       
                          is_staff = is_staff,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):  
    email = models.EmailField(max_length=127, unique=True, null=False, blank=False)
    username = models.CharField(max_length=100,  blank=False, null=True)
    sys_id = models.AutoField(primary_key=True, blank=True)        
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)

    phone = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    other_name = models.CharField(max_length=100,  blank=True)
    date_of_birth = models.DateField( blank=True, null=True)
    gender = models.CharField(
        max_length=1, 
        choices=settings.GENDER,
         blank=True
    )
    photo_url = models.CharField(max_length=500,  blank=True)
    bio = models.TextField(max_length=500, blank=True)
    uAccountType = models.CharField(
        max_length=8, choices=settings.UACCOUNTTYPE, default=settings.UACCOUNT_CONFIG["UACCOUNTTYPE_DEFAULT"])
    
    
    
    # USERNAME_FIELD = settings.UACCOUNT_CONFIG["USERNAME_FIELD"]
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'is_staff']


    objects = MyUserManager()

    class Meta:
        app_label = "users"
        db_table = "users"


       # HISTORY
    history = HistoricalRecords()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff


class UserDocument(models.Model):
    name = models.CharField(max_length=100)
    file_hash = models.CharField(max_length=500, blank=True)
    purpose = models.CharField(max_length=300)
    url = models.CharField(max_length=200)
       # HISTORY
    history = HistoricalRecords()
    #RELATIONS
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Address(models.Model):
    apartment = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postCode = models.CharField(max_length=100, blank=True)
    zipCode = models.CharField(max_length=100, blank=True)
    
    #RELATIONS
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
      # HISTORY
    history = HistoricalRecords()
