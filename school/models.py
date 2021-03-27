  
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class AbstractTableMeta(models.Model):
    created_at = models.DateField(auto_now_add=True, null = True, blank= True)
    updated_at = models.DateField(auto_now=True, null = True, blank= True)
    created_by = models.ForeignKey('school.User', null= True, blank= True ,
                                   on_delete=models.DO_NOTHING,
                                   related_name='+')
    modified_by = models.ForeignKey('school.User', null = True, blank= True,
                                    on_delete=models.DO_NOTHING,
                                    related_name='+')

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=100)
    bio = models.TextField(default='', blank=True)
    father_name = models.CharField(max_length=100, null=True)
    mother_name = models.CharField(max_length=100, null=True)
    avatar_url = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=50, null=True)
    level = models.IntegerField(null = True, )
    phone = models.CharField(max_length=50, null=True)
    avatar= models.ImageField(upload_to='avatars',)

    def __str__(self):
        return f'{self.name}'


class Certificate(AbstractTableMeta, models.Model):
    name = models.CharField(blank = True, null =True , max_length=50)
    description = models.TextField(blank= True, null =True , max_length= 1000)

    def __str__(self):
        return self.name


class StudentsCertificate(AbstractBaseUser, models.Model):
    user = models.ForeignKey("school.User", null =True, blank = True ,on_delete=models.CASCADE)
    certificate = models.ForeignKey("school.Certificate", null =True, blank = True ,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} got {self.certificate}'


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    

