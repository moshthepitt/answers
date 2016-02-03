from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'userprofile', 'quiz', 'sitting']

admin.site.register(Review, ReviewAdmin)
