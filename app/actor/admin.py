from django.contrib import admin

from actor.models import Actor


class ActorAdmin(admin.ModelAdmin):
    class Meta:
        model = Actor

    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']


admin.site.register(Actor, ActorAdmin)
