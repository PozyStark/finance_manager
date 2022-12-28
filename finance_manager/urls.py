from django.urls import path

from finance_manager.views import ExpensesAPIUpdate, ExpensesAPIList, FinanceUserRegisterAPIView, \
    FinanceUserUpdateAPIView

urlpatterns = [
    path('register/', FinanceUserRegisterAPIView.as_view(), name='register'),
    path('update/', FinanceUserUpdateAPIView.as_view(), name='update'),
    path('expenseslist/', ExpensesAPIList.as_view(), name='expenses')
]
