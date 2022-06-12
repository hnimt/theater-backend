from django.contrib import admin

from director.models import Director


class DirectorAdmin(admin.ModelAdmin):
    class Meta:
        model = Director

    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']


admin.site.register(Director, DirectorAdmin)
