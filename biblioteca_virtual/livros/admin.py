from django.contrib import admin
from .models import Livros
from django.contrib.admin.filters import SimpleListFilter
# Register your models here.

class CustomFilter(SimpleListFilter):
    title = "Filtro Customizado"
    parameter_name = "custom"
    def lookups(self, request, model_admin):
        return (
            ("value_01", "Titulo"),
            ("value_02", "Autor"),
            ("value_03", "Ano de Edição"),
        )
    def queryset(self, request, queryset):
        if self.value() == "value_01":
            queryset = queryset.order_by("titulo")
        elif self.value() == "value_02":
            queryset = queryset.order_by("autor")
        elif self.value() == "value_03":
            queryset = queryset.order_by("ano_edicao")
        return queryset 

class LivrosAdmin(admin.ModelAdmin):
    list_filter = ['autor', CustomFilter]
    search_fields = ['titulo', 'autor', 'ano_edicao']
    

admin.site.register(Livros, LivrosAdmin)