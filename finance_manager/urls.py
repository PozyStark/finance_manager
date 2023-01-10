from django.urls import path

from finance_manager.views import \
    UserRegisterAPIView, \
    UserProfileUpdateAPIView, \
    UserChangePasswordAPIView, \
    ExpensesAPIView, RegularExpensesAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('updateprofile/', UserProfileUpdateAPIView.as_view(), name='update_profile'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change_password'),

    path('expenses/', ExpensesAPIView.as_view(), name='expenses'),
    path('expenses/<int:id>/', ExpensesAPIView.as_view(), name='expenses_detail'),

    path('regular-expenses/', RegularExpensesAPIView.as_view(), name='regular_expenses'),
    path('regular-expenses/<int:id>/', RegularExpensesAPIView.as_view(), name='regular_expenses_detail'),
]
