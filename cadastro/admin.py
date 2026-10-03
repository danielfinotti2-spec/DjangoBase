from django.contrib import admin

from .models import Pessoa, Telefone


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'idade']
    search_fields = ['nome', 'email']
    inlines = [TelefoneInline]


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['numero', 'pessoa']
    search_fields = ['numero', 'pessoa__nome']
