from .models import Review


def review_groups(name, sitting, quiz, group=None):
    """
    Bulk create reviews
    Usage:
        from questions.models import Quiz, Sitting
        from users.models import UserGroup

        from reviews.utils import review_groups

        quiz = Quiz.objects.get(pk=7)
        sitting = Sitting.objects.get(pk=5)
        group = UserGroup.objects.get(pk=10)
        name = "Accounts"

        review_groups(name=name, sitting=sitting, quiz=quiz, group=group)
    """
    if sitting.customer == quiz.customer:
        if not group or (group and (sitting.customer == quiz.customer == group.customer)):
            r = Review()
            r.title = name
            r.customer = sitting.customer
            r.sitting = sitting
            r.quiz = quiz
            r.save()
            if not group:
                r.public = True
                r.save()
            else:
                userprofiles = group.userprofile_set.all()
                r.reviewers.add(*list(userprofiles))
