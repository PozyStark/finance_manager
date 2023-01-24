from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from finance_manager.serializers import ExpenseSerializer, \
    UserRegisterSerializer, \
    UserProfileUpdateSerializer, \
    UserChangePasswordSerializer, RegularExpenseSerializer, CashIncomeSerializer, BankSerializer

from finance_manager.models import Expenses, User, RegularExpenses, CashIncomes, Banks
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserRegisterAPIView(CreateAPIView):
    """Обработчик для регистрации пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.save()
            data['response'] = 'user was created'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data)


class UserProfileUpdateAPIView(GenericAPIView):
    """ Обработчик обновления профиля для авторизованных пользователей
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileUpdateSerializer

    def put(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserProfileUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(request.user, serializer.data)
            return Response({'detail': 'profile was updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class UserChangePasswordAPIView(GenericAPIView):
    """ Обработчик смены пароля для авторизованных пользователей
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def put(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update(request.user, serializer.data)
            return Response({'detail': 'password changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class ExpensesAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get(self, request, id=None):
        user = request.user
        if id:
            expense = get_object_or_404(Expenses, user=user, id=id)
            return Response(
                {
                    'expense': {
                            'id': expense.id,
                            'name': expense.name,
                            'amount': expense.amount,
                            'date': expense.date
                        }
                }, status=status.HTTP_200_OK
            )

        expenses = Expenses.objects.filter(user=user)
        return Response(
            {'expenses': expenses.values('id', 'name', 'amount', 'date')},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        expenses = request.data.get('expenses')
        if expenses:
            serializer = self.serializer_class(
                data=expenses,
                context={'request': request},
                many=True
            )
        else:
            serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )

        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(
                {'detail': 'expense create'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)

    def put(self, request, id):

        user = request.user
        expense = get_object_or_404(Expenses, user=user, id=id)

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.update(expense, serializer.data)
            return Response({'detail': 'expense updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, id):
        user = request.user
        expense = get_object_or_404(Expenses, user=user, id=id)
        expense.delete()
        return Response({'detail': f'expense id:{id} deleted'})


class RegularExpensesAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = RegularExpenseSerializer

    def get(self, request, id=None):
        user = request.user
        if id:
            regular_expense = get_object_or_404(RegularExpenses, user=user, id=id)
            return Response(
                {
                    'regular_expense': {
                        'id': regular_expense.id,
                        'name': regular_expense.name,
                        'amount': regular_expense.amount
                    }
                }, status=status.HTTP_200_OK
            )

        regular_expenses = RegularExpenses.objects.filter(user=user)
        return Response(
            {
                'regular_expenses': regular_expenses.values('id', 'name', 'amount')
            }
        )

    def post(self, request):
        regular_expenses = request.data.get('regular_expenses')
        if regular_expenses:
            serializer = self.serializer_class(
                data=regular_expenses,
                context={'request': request},
                many=True
            )
        else:
            serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'detail': 'regular expense create'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    def put(self, request, id=None):

        user = request.user
        regular_expense = get_object_or_404(RegularExpenses, user=user, id=id)
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.update(regular_expense, serializer.data)
            return Response({'detail': 'regular expense updated'})
        return Response(serializer.errors)

    def delete(self, request, id=None):
        user = request.user
        regular_expense = get_object_or_404(RegularExpenses, user=user, id=id)
        regular_expense.delete()
        return Response({'detail': f'regular expense id:{id} deleted'})


class CashIncomesAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CashIncomeSerializer

    def get(self, request):
        user = request.user
        if id:
            cash_income = get_object_or_404(CashIncomes, user=user, id=id)
            return Response(
                {
                    'cash_income': {
                        'id': cash_income.id,
                        'name': cash_income.name,
                        'amount': cash_income.amount,
                        'date': cash_income.date
                    }
                }, status=status.HTTP_200_OK
            )

        cash_incomes = CashIncomes.objects.filter(user=user)
        return Response(
            {
                'cash_incomes': cash_incomes.values('id', 'name', 'amount', 'date')
            }
        )

    def post(self, request):
        cash_incomes = request.data.get('cash_incomes')
        if cash_incomes:
            serializer = self.serializer_class(
                data=cash_incomes,
                context={'request': request},
                many=True
            )
        else:
            serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'detail': 'cash incomes create'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        cash_income = get_object_or_404(CashIncomes, user=user, id=id)
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.update(CashIncomes, serializer.data)
            return Response({'detail': 'cash income updated'})
        return Response(serializer.errors)

    def delete(self, request):
        user = request.user
        cash_income = get_object_or_404(CashIncomes, user=user, id=id)
        cash_income.delete()
        return Response({'detail': f'cash income id:{id} deleted'})


class BanksAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BankSerializer

    def get(self, request):
        user = request.user
        if id:
            bank = get_object_or_404(Banks, user=user, id=id)
            return Response(
                {
                    'cash_income': {
                        'id': bank.id,
                        'name': bank.name,
                        'required_amount': bank.required_amount,
                        'available_amount': bank.available_amount
                    }
                }, status=status.HTTP_200_OK
            )

        banks = Banks.objects.filter(user=user)
        return Response(
            {
                'banks': banks.values('id', 'name', 'required_amount', 'available_amount')
            }
        )

    def post(self, request):
        banks = request.data.get('banks')
        if banks:
            serializer = self.serializer_class(
                data=banks,
                context={'request': request},
                many=True
            )
        else:
            serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'detail': 'banks create'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        bank = get_object_or_404(Banks, user=user, id=id)
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.update(Banks, serializer.data)
            return Response({'detail': 'bank updated'})
        return Response(serializer.errors)

    def delete(self, request):
        user = request.user
        bank = get_object_or_404(Banks, user=user, id=id)
        bank.delete()
        return Response({'detail': f'bank id:{id} deleted'})
