from django.db import models
from django.core.validators import RegexValidator 
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from django.contrib.auth import get_user_model
# My model
phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")
class User(AbstractUser):
    phone_number = models.CharField(validators=[phone_regex], max_length=15, verbose_name='Номер телефона')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    def __str__(self):
        return f'Пользователи'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
# user = get_user_model()
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_users', verbose_name='Пользователь')
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    is_completed = models.BooleanField(default=False,verbose_name='Выполнен' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True, verbose_name='Фото')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Cписок дел'
        verbose_name_plural = 'Cписки дел'
