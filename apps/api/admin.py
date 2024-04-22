from django.contrib import admin
from .models import User, Todo
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'email', 'created_at']
    
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'description', 'is_completed', 'created_at']
    
    # Эта функция позволяет видеть картинку в админ панеле
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}', width='60' />".format(obj.image.url))
        return "None"
    image_show.__name__ = "Картинка"