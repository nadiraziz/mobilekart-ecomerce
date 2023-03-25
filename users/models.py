
from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db.models.signals import post_save
from PIL import Image

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None, password2=None):
        """
        Creates and saves a User with the given email, username, phone_number and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=email,
            username=username,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password=None,):
        """
        Creates and saves a superuser with the given email, name, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):

    """Profile mode with name, email, phone_number number , 
    billing address, shipping address, profile image."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    username = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255)
    phone_number = models.CharField( blank=True, max_length=255)
    billing_address = models.CharField( max_length=50)
    shipping_address = models.CharField( max_length=50)
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True, default='profile/user-default.png',)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'user_profile'
        
        
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

