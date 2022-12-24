from django.contrib import admin
from finance_manager.models import FinanceManagerUser,\
    Expenses, RegularExpenses, CashIncomes, Banks

admin.site.register(FinanceManagerUser)
admin.site.register(Expenses)
admin.site.register(RegularExpenses)
admin.site.register(CashIncomes)
admin.site.register(Banks)
