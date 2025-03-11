from django.contrib import admin
from .models import Service, Category, Photo

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ('title', 'photo')