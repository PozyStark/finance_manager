from django.urls import path

from finance_manager.views import \
    UserRegisterAPIView, \
    UserProfileUpdateAPIView, \
    UserChangePasswordAPIView, \
    ExpensesAPIView, RegularExpensesAPIView, CashIncomesAPIView, BanksAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('updateprofile/', UserProfileUpdateAPIView.as_view(), name='update_profile'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change_password'),

    path('expenses/', ExpensesAPIView.as_view(), name='expenses'),
    path('expenses/<int:id>/', ExpensesAPIView.as_view(), name='expenses_detail'),

    path('regular-expenses/', RegularExpensesAPIView.as_view(), name='regular_expenses'),
    path('regular-expenses/<int:id>/', RegularExpensesAPIView.as_view(), name='regular_expenses_detail'),

    path('cash-incomes/', CashIncomesAPIView.as_view(), name='cash_incomes'),
    path('cash-incomes/<int:id>/', CashIncomesAPIView.as_view(), name='cash_incomes_detail'),

    path('banks/', BanksAPIView.as_view(), name='banks'),
    path('banks/<int:id>/', BanksAPIView.as_view(), name='banks_detail')
]
