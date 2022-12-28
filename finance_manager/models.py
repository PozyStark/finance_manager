from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class FinanceUserManager(BaseUserManager):
    """Менеджер для создания кастомного пользователя
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_stuff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class FinanceUser(AbstractBaseUser, PermissionsMixin):
    """Модель кастомного пользователя для авторизации по полю email
    """

    email = models.EmailField(max_length=255, null=False, blank=False, unique=True, db_index=True)
    number = models.CharField(max_length=18, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True, auto_now=True)

    objects = FinanceUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number']

    class Meta:
        verbose_name = 'FinanceUser'
        verbose_name_plural = 'FinanceUsers'


class Expenses(models.Model):
    """Модель содержит все возможные траты пользователя"""

    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} [{self.name}] [{self.amount}]'

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'


class RegularExpenses(models.Model):
    """Модель содержит регулярные траты пользователя"""

    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return f'{self.user.email} [{self.name}] [{self.amount}]'

    class Meta:
        verbose_name = 'RegularExpense'
        verbose_name_plural = 'RegularExpenses'


class CashIncomes(models.Model):
    """Модель содержит все возможные доходы пользователя"""

    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)
    regular = models.BooleanField(default=False, null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f'{self.user.email} [{self.name}] [{self.amount}]'

    class Meta:
        verbose_name = 'CashIncome'
        verbose_name_plural = 'CashIncomes'


class Banks(models.Model):
    """Модель содержит цели для накопления"""

    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    required_amount = models.FloatField(default=0, null=False, blank=False)
    available_amount = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return f'{self.user.email} [{self.name}] [{self.required_amount}] [{self.available_amount}]'

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
