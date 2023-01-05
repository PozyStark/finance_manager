from django.urls import path

from finance_manager.views import \
    FinanceUserRegisterAPIView, \
    FinanceUserProfileUpdateAPIView, \
    FinanceUserChangePasswordAPIView, \
    ExpensesAPIList, \
    ExpenseDetailAPIView

urlpatterns = [
    path('register/', FinanceUserRegisterAPIView.as_view(), name='register'),
    path('updateprofile/', FinanceUserProfileUpdateAPIView.as_view(), name='update_profile'),
    path('changepassword/', FinanceUserChangePasswordAPIView.as_view(), name='change_password'),

    path('expenseslist/', ExpensesAPIList.as_view(), name='expenses_list'),
    path('expensedetail/<int:id>/', ExpenseDetailAPIView.as_view(), name='expense_detail')
]
