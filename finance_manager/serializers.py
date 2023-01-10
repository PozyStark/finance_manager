import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from finance_manager.models import Expenses, User, RegularExpenses
from django.contrib.auth import authenticate
from finance_manager.validators import PasswordValidation


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации кастомного пользователя
    """

    confirm_password = serializers.CharField(max_length=255, required=True)

    def validate_password(self, password):
        return PasswordValidation(
            password=password,
            length=8,
            excluded_chars=[PasswordValidation.RUS_CHARS_LOW, PasswordValidation.RUS_CHARS_UPPER],
            must_contain=PasswordValidation.SPECIAL_CHARACTERS
        ).validate()

    def save(self, **kwargs):
        finance_user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise ValidationError({'confirm_password': ['password matching error']})

        finance_user.set_password(password)
        finance_user.save()
        return finance_user

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password'
        ]


class UserProfileUpdateSerializer(serializers.Serializer):
    """ Сериализатор для обновления информации о пользователе
    """

    email = serializers.EmailField(max_length=255, required=False, allow_blank=False, allow_null=False)
    number = serializers.CharField(max_length=18, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.number = validated_data.get('number', instance.number)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        return instance

    def create(self, validated_data):
        pass


class UserChangePasswordSerializer(serializers.Serializer):
    """ Сериализотор для обновления пароля
    """

    old_password = serializers.CharField(
        max_length=255,
        required=True,
        write_only=True,
        allow_blank=False,
        allow_null=False
    )
    new_password = serializers.CharField(max_length=255, required=True, write_only=True)
    confirm_password = serializers.CharField(max_length=255, required=True, write_only=True)

    def validate_old_password(self, old_password):
        user = self.context['request'].user
        user = authenticate(email=user.email, password=old_password)
        if user:
            return old_password
        raise ValidationError('incorrect password')

    def validate_new_password(self, new_password):
        return PasswordValidation(
            password=new_password,
            length=8,
            excluded_chars=[PasswordValidation.RUS_CHARS_LOW, PasswordValidation.RUS_CHARS_UPPER],
            must_contain=PasswordValidation.SPECIAL_CHARACTERS
        ).validate()

    def update(self, instance, validated_data):
        old_password = self.validated_data['old_password']
        new_password = self.validated_data['new_password']
        confirm_password = self.validated_data['confirm_password']

        if new_password != confirm_password:
            raise ValidationError({'confirm_password': ['password matching error']})

        instance.set_password(new_password)
        instance.save()
        return instance

    def create(self, validated_data):
        pass


class ExpenseSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    amount = serializers.FloatField(required=True)
    date = serializers.DateField(required=False)

    def create(self, validated_data):
        user = self.context['request'].user
        return Expenses.objects.create(
            user=user,
            name=validated_data['name'],
            amount=validated_data['amount'],
            date=validated_data.get('date', datetime.date.today())
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class RegularExpenseSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    amount = serializers.FloatField(required=True)

    def create(self, validated_data):
        user = self.context['request'].user
        return RegularExpenses.objects.create(
            user=user,
            name=validated_data['name'],
            amount=validated_data['amount']
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance
