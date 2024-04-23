from django.contrib import admin
from .models import Todo, User
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'description', 'is_completed', 'created_at']
    
    # Эта функция позволяет видеть картинку в админ панеле
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}', width='60' />".format(obj.image.url))
        return "None"
    image_show.__name__ = "Картинка"
    
@admin.register(User)
class AdminUSer(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']