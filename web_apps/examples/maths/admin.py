from django.contrib import admin
from .models import Maths
# Register your models here.

class AdminMath(admin.ModelAdmin):
    list_display = ['operacja','a','b','wynik','created']
    list_filter = ['operacja']
    search_fields = ['a']

admin.site.register(Maths,AdminMath)