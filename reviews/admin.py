from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['userprofile', 'quiz', 'title', 'sitting']

admin.site.register(Review, ReviewAdmin)
