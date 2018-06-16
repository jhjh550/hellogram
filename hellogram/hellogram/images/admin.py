from django.contrib import admin
from . import models 


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display_links = (
        'location',
        'caption',
    )

    list_display = (
        'creator',
        'created_at',
        'updated_at',
        'file',
        'location',
        'caption'
    ) 


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'created_at',
        'updated_at',
        'image',
    ) 


@admin.register(models.Comment)
class CommentAdming(admin.ModelAdmin):

    list_display = (
        'creator',
        'created_at',
        'updated_at',
        'message',
        'image',
    ) 


    
