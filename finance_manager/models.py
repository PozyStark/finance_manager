from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO: "Создать кастомного пользователя и связать модели"


class FinanceUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_stuff') is not True:
            raise ValueError('Superuser has to have is_stuff being True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being True')

        return self.create_user(email=email, password=password, **extra_fields)


class FinanceManagerUser(AbstractUser):
    """Модель пользователя с аутентификацией по email"""

    GENDERS = (
        ('none', 'None'),
        ('male', 'Male'),
        ('female', 'Female')
    )

    objects = FinanceUserManager
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    username = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(default=0, null=False, blank=False)
    gender = models.CharField(max_length=255, choices=GENDERS, default=GENDERS[0], null=False, blank=False)
    time_created = models.DateField(auto_now_add=True, null=False, blank=False)
    time_updated = models.DateField(auto_now=True, null=False, blank=False)
    last_login = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
#
#
# class Expenses(models.Model):
#     """Модель содержит все возможные траты пользователя"""
#
#     # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False, blank=False)
#     amount = models.FloatField(default=0, null=False, blank=False)
#     date = models.DateField(auto_created=True)
#
#     class Meta:
#         verbose_name = 'Expense'
#         verbose_name_plural = 'Expenses'
#
#
# class RegularExpenses(models.Model):
#     """Модель содержит регулярные траты пользователя"""
#
#     # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False, blank=False)
#     amount = models.FloatField(default=0, null=False, blank=False)
#
#     class Meta:
#         verbose_name = 'RegularExpense'
#         verbose_name_plural = 'RegularExpenses'
#
#
# class CashIncomes(models.Model):
#     """Модель содержит все возможные доходы пользователя"""
#
#     # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False, blank=False)
#     amount = models.FloatField(default=0, null=False, blank=False)
#     regular = models.BooleanField(default=False, null=False, blank=False)
#     date = models.DateField(auto_now=True, null=False, blank=False)
#
#     class Meta:
#         verbose_name = 'CashIncome'
#         verbose_name_plural = 'CashIncomes'
#
#
# class Banks(models.Model):
#     """Модель содержит цели для накопления"""
#
#     # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False, blank=False)
#     required_amount = models.FloatField(default=0, null=False, blank=False)
#     available_amount = models.FloatField(default=0, null=False, blank=False)
#
#     class Meta:
#         verbose_name = 'Bank'
#         verbose_name_plural = 'Banks'
#
#
# class Genders(models.Model):
#     """Модель содержит пол пользователя"""
#
#     gender = models.CharField(max_length=255, null=False, blank=False)
#
#     class Meta:
#         verbose_name = 'Gender'
#         verbose_name_plural = 'Genders'
#
#
