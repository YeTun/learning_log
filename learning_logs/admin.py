from django.contrib import admin
from learning_logs.models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added', 'owner')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)

