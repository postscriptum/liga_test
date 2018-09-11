from django.contrib import admin
from .models import Source, Document


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'user', 'added', 'updated')
    readonly_fields = ('edit_count',)
    search_fields = ['title', 'text']
    list_filter = ('source', 'user', 'created', 'updated')
