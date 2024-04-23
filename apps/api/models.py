from django.db import models
from django.core.validators import RegexValidator 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")
    age = models.PositiveIntegerField(verbose_name='Возраст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    email = models.EmailField(verbose_name='Эл.почта')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, verbose_name='Номер телефона')
    def __str__(self):
        return f'Пользователи'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    

class Todo(models.Model):
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
