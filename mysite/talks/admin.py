from django.contrib import admin

from talks.models import Event, Talk


class EventInlineAdmin(admin.StackedInline):
    model = Event


class TalkAdmin(admin.ModelAdmin):
    inlines = [EventInlineAdmin]


admin.site.register(Talk, TalkAdmin)
