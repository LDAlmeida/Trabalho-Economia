from django.contrib import admin

from economia.models import Person

# Register your models here.

@admin.action(description='Prever entrada selecionada')
def prever(modeladmin, request, queryset):
    for person in queryset:
        person.prever_emprego()
class PersonAdmin(admin.ModelAdmin):
    actions = [prever]

admin.site.register(Person,PersonAdmin)