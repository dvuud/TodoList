from django.db import models
from django.core.validators import RegexValidator # 

class User(models.Model):
    phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")
    age = models.DecimalField(verbose_name='Возраст', decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    
    def __str__(self):
        return f'Пользователи'
    class Meat:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    

class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True, verbose_name='Фото')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Cписок дел'
        verbose_name = 'Cписки дел'
    
