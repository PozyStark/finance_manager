from django.contrib import admin
from finance_manager.models import Expenses, RegularExpenses, CashIncomes, Banks, User

admin.site.register(User)
admin.site.register(Expenses)
admin.site.register(RegularExpenses)
admin.site.register(CashIncomes)
admin.site.register(Banks)
