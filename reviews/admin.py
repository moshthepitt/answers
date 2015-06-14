from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
