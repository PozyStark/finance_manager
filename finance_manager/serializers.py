from rest_framework import serializers
from finance_manager.models import Expenses, FinanceUser


class FinanceUserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для кастомного пользователя
    """

    password_confirm = serializers.CharField(max_length=255, required=True)

    def save(self, **kwargs):
        finance_user = FinanceUser(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({password: 'password matching error'})

        finance_user.set_password(password)
        finance_user.save()
        return finance_user

    class Meta:
        model = FinanceUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirm'
        ]


class FinanceUserUpdateSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255, required=False, allow_blank=True)
    number = serializers.CharField(max_length=18, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    password = serializers.CharField(required=False, write_only=True, allow_blank=True)
    password_confirm = serializers.CharField(required=False, write_only=True, allow_blank=True)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', None)
        password_confirm = validated_data.get('password_confirm', None)

        if password != password_confirm:
            raise serializers.ValidationError({password: 'password matching error'})

        if password is not None and password_confirm is not None:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class ExpensesSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
    date = serializers.DateField(required=False)

    def create(self, validated_data):
        return Expenses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class ExpensesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id', 'user', 'name', 'amount']
