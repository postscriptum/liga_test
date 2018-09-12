from datetime import datetime, timedelta, timezone
from django.contrib import messages
from django.contrib import admin
from .models import Source, Document


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'user', 'added', 'updated')
    readonly_fields = ('edit_count', 'user')
    search_fields = ['title', 'text']
    list_filter = ('source', 'user', 'created', 'updated')

    def save_model(self, request, obj, form, change):
        if change and not request.user.is_superuser:
            delta = datetime.now(timezone(timedelta(hours=3))) - obj.added
            if delta.total_seconds() > 60:  # 3600
                self.message_user(request, 'Changes are not allowed!',
                                  level=messages.WARNING)
                return
        if change:
            obj.edit_count += 1
        else:
            obj.user = request.user
        super().save_model(request, obj, form, change)
