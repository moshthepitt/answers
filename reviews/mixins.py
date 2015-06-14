from django.shortcuts import redirect

from answers.models import Answer


class PeerReviewMixin(object):
    """
    Control who can take a peer review
    """

    def dispatch(self, *args, **kwargs):
        review = self.get_object()
        # dont allow a non reviewer to review
        if self.request.user not in review.reviewers.all():
            return redirect('home')
        # not more than one reviews
        if Answer.objects.filter(user=self.request.user).filter(peer_review=review).exists():
            return redirect('home')
        return super(PeerReviewMixin, self).dispatch(*args, **kwargs)
