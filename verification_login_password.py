class User:
    """
    Класс для хранения информации о пользователе с возможностью проверки пароля и изменения учетных данных

    Обеспечивает хранение основных данных пользователя (name, email, role), а также приватных атрибутов
    логина и пароля. При установке или изменении пароля выполняется проверка его соответствия
    заданным требованиям по длине и типу.

    Атрибуты:
        name (str): Имя пользователя
        email (str): Электронная почта пользователя
        role (str): Должность пользователя

    Приватные атрибуты: 
        __login (str): Логин пользователя
        __password (str): Пароль пользователя

    Методы:
        get_login_password() -> tuple: Возвращает логин и пароль пользователя
        set_login_password(login: str, password: str): Устанавливает новый логин и пароль после проверки

    Приватные методы:
        __validate_login(login: str): Проверяет логин на тип и наличия символов
        __validate_password(password: str): Проверяет пароль пользователя на тип и длину

    Исключения:
        TypeError: Логин / пароль не строки
        ValueError: Пустой логин
        AttributeError: Пароль не соответствует длине
    """
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login: str, password: str, name: str, email: str, role: str):
        self.__validate_login(login)
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    def get_login_password(self) -> tuple:
        """Возвращает логин и пароль"""
        return self.__login, self.__password
    
    @classmethod
    def __validate_login(self, login: str):
        """Проверяет валидность логина
        
        Проверка логина включает:
            - Тип должен быть str
            - Логин не пустая строка

        Args:
            login (str): Логин для проверки

        Raises:
            TypeError: Если не соответствует типу
            ValueError: Если пустая строка
        """
        if not isinstance(login, str):
            raise TypeError('Логин должен быть строкой')
        
        if not login.strip():
            raise ValueError('Логин не может быть пустым')
        
    @classmethod
    def __validate_password(cls, password: str):
        """Проверяет валидность пароля

        Проверка пароля включает:
            - Тип должен быть str
            - Длина пароля от 5 до 16 символов

        Args:
            password (str): Пароль для проверки

        Raises:
            TypeError: Если пароль не является строкой
            AttributeError: Если длина пароля не в допустимом диапазоне
        """
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой!')
        
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN):
            raise AttributeError(
                f'Длина пароля должна быть от {cls.PASSWORD_MIN_LEN} до {cls.PASSWORD_MAX_LEN} символов')
        
    def set_login_password(self, login: str, password: str):
        """Устанавливает новый логин и пароль после проверки

            Args:
                login (str): Новый логин пользователя
                password (str): Новый пароль пользователя
            
            Raises:
                TypeError: Если логин или пароль не являются строками
                ValueError: Если логин пустой
                AttributeError: Если длина пароля не в допустимом диапазоне
        """
        self.__validate_login(login)
        self.__validate_password(password)
        self.__login = login
        self.__password = password

# Проверочный код
    
u1 = User("JohnD", "mlo123", "John Doe", "john.doe@example.com", 'TechLead')

# Позитивные тесты

u1.set_login_password('New login', 'NewPassword')
print(u1.get_login_password())

# Негативные тесты

try:
    User(123, 'pass', "John Doe", "john.doe@example.com", 'TechLead')
except TypeError as e: 
    print(e)  # TypeError (логин)

try:
    u1.set_login_password('', 'pass')
except ValueError as e:
    print(e) # ValueError (логин)

try:
    u1.set_login_password('New person', 123)
except TypeError as e:
    print(e) # TypeError (пароль)

try:
    u1.set_login_password('New person', '1234')
except AttributeError as e:
    print(e) # AttributeError (длина пароля)