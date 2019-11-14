from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, name=None, password=None):
        """
        Creates and saves a User with the given cpf and password.
        """
        if not username:
            raise ValueError('Users must have a USERNAME')

        user = self.model(
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password):
        """
        Creates and saves a superuser with the given cpf and password.
        """
        user = self.create_user(
            username,
            name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField('Nome', max_length=50)
    username = models.CharField('Nome de Usuário', max_length=30, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin

    class Meta:
        ordering = ['name']
