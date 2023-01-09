from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from finance_manager.serializers import ExpenseSerializer,\
    UserRegisterSerializer, \
    UserProfileUpdateSerializer,\
    UserChangePasswordSerializer

from finance_manager.models import Expenses, User
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
            return Response({'response': 'profile was updated'}, status=status.HTTP_200_OK)
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
            return Response({'response': 'password changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class ExpensesAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get(self, request):
        user = request.user
        expenses = Expenses.objects.filter(user=user)
        return Response(
            {
                'expenses': expenses.values('id', 'name', 'amount', 'date')
            }, status=status.HTTP_200_OK
        )


class AddExpenseAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def post(self, request):

        if request.data.get('expenses'):
            serializer = ExpenseSerializer(data=request.data['expenses'], context={'request': request}, many=True)
        else:
            serializer = ExpenseSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'response': 'expense create'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ExpenseDetailAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get(self, request, id):
        user = request.user
        expense = Expenses.objects.get(user=user, id=id)
        return Response(
            {
                'expense': {
                    'id': expense.id,
                    'name': expense.name,
                    'amount': expense.amount,
                    'date': expense.date
                }
            }
        )


class ExpensesAPIUpdate(UpdateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


