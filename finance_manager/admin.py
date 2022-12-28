from django.contrib import admin
from finance_manager.models import Expenses, RegularExpenses, CashIncomes, Banks, FinanceUser

admin.site.register(FinanceUser)
admin.site.register(Expenses)
admin.site.register(RegularExpenses)
admin.site.register(CashIncomes)
admin.site.register(Banks)
