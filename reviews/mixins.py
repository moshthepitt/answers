from django.shortcuts import redirect


class PeerReviewMixin(object):
    """
    Do not allow users who are not reviewers to access a peer review
    """

    def dispatch(self, *args, **kwargs):
        review = self.get_object()

        if self.request.user not in review.reviewers.all():
            return redirect('home')
        return super(PeerReviewMixin, self).dispatch(*args, **kwargs)
