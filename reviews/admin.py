from django.contrib import admin

from reviews.models import PeerReview


class PeerReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(PeerReview, PeerReviewAdmin)
