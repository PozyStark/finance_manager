from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO: "Создать кастомного пользователя и связать модели"

# class EmailUser(AbstractUser):
#     pass
#
#     def __str__(self):
#         return self.username


class Expenses(models.Model):
    """Модель содержит все возможные траты пользователя"""

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)
    date = models.DateField(auto_created=True)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'


class RegularExpenses(models.Model):
    """Модель содержит регулярные траты пользователя"""

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'RegularExpense'
        verbose_name_plural = 'RegularExpenses'


class CashIncomes(models.Model):
    """Модель содержит все возможные доходы пользователя"""

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'CashIncome'
        verbose_name_plural = 'CashIncomes'


class Banks(models.Model):
    """Модель содержит цели для накопления"""

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    required_amount = models.FloatField(default=0, null=False, blank=False)
    available_amount = models.FloatField(default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'


class Genders(models.Model):
    """Модель содержит пол пользователя"""

    gender = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'


