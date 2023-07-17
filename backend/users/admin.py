from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "password")
    list_filter = (
        "first_name",
        "email",
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "user",
    )
    search_fields = (
        "user",
        "author",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
