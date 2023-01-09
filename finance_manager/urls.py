from django.urls import path

from finance_manager.views import \
    UserRegisterAPIView, \
    UserProfileUpdateAPIView, \
    UserChangePasswordAPIView, \
    ExpensesAPIView, \
    ExpenseDetailAPIView,\
    AddExpenseAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('updateprofile/', UserProfileUpdateAPIView.as_view(), name='update_profile'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change_password'),

    path('expenses/', ExpensesAPIView.as_view(), name='expenses'),
    path('addexpense/', AddExpenseAPIView.as_view(), name='add_expense'),
    path('expensedetail/<int:id>/', ExpenseDetailAPIView.as_view(), name='expense_detail')
]
