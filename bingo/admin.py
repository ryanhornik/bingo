from django.contrib import admin
from bingo.models import *


# Register your models here.
admin.site.register(Game)


class TermAdmin(admin.ModelAdmin):
    list_display = ('text', 'game')
admin.site.register(Term, TermAdmin)

admin.site.register(OrderedTerm)
admin.site.register(Card)
