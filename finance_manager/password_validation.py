from rest_framework.serializers import ValidationError


class PasswordValidation:
    """ Класс валидации пароля. Выполняет валидацию по трем критериям.
        Длинна пароля должна быть не менее чем length символов.
        Пароль не должен содержать кириличекских символов любого регистра.
        Пароль должен содержать хотябы один спецсимвол.
    """

    RUS_CHARS_LOW = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    RUS_CHARS_UPPER = RUS_CHARS_LOW.upper()
    SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "&", "*", "?", ".", "/", "\\", "|", "^", ":", ";"]

    def __init__(self, password: str,  **kwargs):
        self.password = password
        self.length = kwargs.get('length', None)
        self.excluded_chars = kwargs.get('excluded_chars', None)
        self.must_contain = kwargs.get('must_contain', None)
        self._validate_types()

    def _validate_types(self):
        if type(self.password) is not str:
            raise TypeError({self.password: 'Must be string type'})
        if (type(self.length) is not int) and (self.length is not None):
            raise TypeError({self.length: 'Must be integer type'})
        if type(self.excluded_chars) is not list and (self.excluded_chars is not None):
            raise TypeError({self.excluded_chars: 'Must be list type'})
        if type(self.must_contain) is not list and (self.must_contain is not None):
            raise TypeError({self.length: 'Must be list type'})

    def _length_validation(self) -> bool:
        if self.length is None:
            return True
        if len(self.password) < self.length:
            return False
        return True

    def _rus_chars_validation(self) -> bool:
        if self.excluded_chars is None:
            return True
        excluded = list()
        for excluded_chars in self.excluded_chars:
            excluded += excluded_chars
        for excluded_char in excluded:
            if excluded_char in self.password:
                return False
        return True

    def _special_chars_validation(self) -> bool:
        if self.must_contain is None:
            return True
        for char in self.must_contain:
            if char in self.password:
                return True
        return False

    def validate(self):
        if self._length_validation() is False:
            raise ValidationError(f'password must contain at least {self.length} characters')
        if self._rus_chars_validation() is False:
            raise ValidationError(f'password can\'t contain {self.excluded_chars}')
        if self._special_chars_validation() is False:
            raise ValidationError(f'password must contain at least one of the characters {self.must_contain}')
        return self.password
