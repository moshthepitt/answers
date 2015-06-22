from django.shortcuts import redirect

from answers.models import Answer


class ReviewMixin(object):
    """
    Control who can take a peer review
    """

    def dispatch(self, *args, **kwargs):
        review = self.get_object()
        # dont allow a non reviewer to review
        if review.reviewers.all() and (self.request.user.userprofile not in review.reviewers.all()):
            return redirect('dashboard')
        # not more than one reviews
        if Answer.objects.filter(userprofile=self.request.user.userprofile).filter(review=review).exists():
            return redirect('dashboard')
        return super(ReviewMixin, self).dispatch(*args, **kwargs)
