from django.contrib import admin

# Register your models here.
from webapp.models import Picture, Album


class PictureAdmin(admin.ModelAdmin):
    list_display = ['image', 'signature', 'created_at']
    readonly_fields = ['created_at', 'author', 'album']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    readonly_fields = ['created_at', 'author']


admin.site.register(Picture, PictureAdmin)
admin.site.register(Album, AlbumAdmin)
