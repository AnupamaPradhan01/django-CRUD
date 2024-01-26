from django.contrib import admin
from crud.models import Student


@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail','stupass')
