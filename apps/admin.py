from django.contrib import admin

from apps.models import Person


@admin.register(Person)
class BlogAdmin(admin.ModelAdmin):
    pass