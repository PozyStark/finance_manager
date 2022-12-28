from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from finance_manager.serializers import ExpensesSerializer, ExpensesModelSerializer, FinanceUserRegisterSerializer, \
    FinanceUserUpdateSerializer
from finance_manager.models import Expenses, FinanceUser
from rest_framework.permissions import IsAuthenticated, AllowAny


class FinanceUserRegisterAPIView(CreateAPIView):
    """Обработчик для регистрации пользователя
    """
    queryset = FinanceUser.objects.all()
    serializer_class = FinanceUserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = FinanceUserRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data)


class FinanceUserUpdateAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FinanceUserUpdateSerializer

    def put(self, request, *args, **kwargs):
        print(request.data)
        serializer = FinanceUserUpdateSerializer(request.data)
        return Response({"response": request.user.email})


class ExpensesAPIList(ListAPIView):

    queryset = Expenses.objects.all()
    serializer_class = ExpensesModelSerializer
    permission_classes = (IsAuthenticated,)


class ExpensesAPIUpdate(UpdateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer


