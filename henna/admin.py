from django.contrib import admin

from henna.models import User
from henna.model.ContactRequest import ContactRequest
from henna.model.GalleryImage import GalleryImage
from henna.model.MainSlideImage import MainSlideImage
from henna.model.PageImage import PageImage

admin.site.site_header = "Lavanya's Henna Admin"
admin.site.index_title = ""
admin.site.site_title = "Lavanya's Henna Admin"

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'phone',
        'is_active',
        'is_superuser',
        'is_staff',
        'created_at',
        'updated_at'
    )
    search_fields = [
        'username',
        'first_name',
        'last_name',
        'phone',
    ]

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_responsed',
        'email',
        'phone',
        'details',
        'response',
        'created_at',
        'updated_at',
    )
    search_fields = [
        'name',
        'email',
        'phone',
    ]

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        'henna_area',
        'package',
        'image',
        'created_at',
        'updated_at'
    )

class MainSlideImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'created_at',
        'updated_at'
    )

class PageImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'created_at',
        'updated_at'
    )


admin.site.register(User, UserAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(MainSlideImage, MainSlideImageAdmin)
admin.site.register(PageImage, PageImageAdmin)
