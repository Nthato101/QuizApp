from django.db import models 
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,UserManager
# Create your models here.


class CustomUserManager(UserManager):
    def make_user(self,email,password,**more_fields):
        if not email:
            raise ValueError("A valid email address was not provided")
        
        email = self.normalize_email(email)
        user=self.model(email=email,**more_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self,email=None,password=None,**more_fields):
        more_fields.setdefault('is_active',True)
        more_fields.setdefault('is_staff',False)
        more_fields.setdefault('is_superuser',False)
        return self.make_user(email,password,**more_fields)
    
    def create_superuser(self,email=None,password=None,**more_fields):
        more_fields.setdefault('is_active',True)
        more_fields.setdefault('is_staff',True)
        more_fields.setdefault('is_superuser',True)
        return self.make_user(email,password,**more_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('Email'),unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Player(AbstractBaseUser):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=150,blank=False, null=True)
    last_name = models.CharField(max_length=150,blank=False, null=True)
    has_played = models.BooleanField(default=False)
    score = models.IntegerField(default=0,blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.first_name} | {self.last_name} | {self.score} | {self.has_played} '

