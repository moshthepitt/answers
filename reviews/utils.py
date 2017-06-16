from .models import Review


def check_equal(lst):
    return lst[1:] == lst[:-1]


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
    proceed = False
    if sitting.customer == quiz.customer:
        if group:
            if isinstance(group, list):
                cus_list = [x.customer for x in group]
                if cus_list and check_equal(cus_list):
                    if cus_list[0] == quiz.customer:
                        proceed = True
            elif isinstance(group, object):
                if group.customer == quiz.customer:
                    proceed = True
        else:
            proceed = True

    if proceed:
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
            if isinstance(group, list):
                done = []
                for g in group:
                    if g not in done:
                        g_userprofiles = g.userprofile_set.all()
                        r.reviewers.add(*list(g_userprofiles))
                        done.append(g)
            elif isinstance(group, object):
                userprofiles = group.userprofile_set.all()
                r.reviewers.add(*list(userprofiles))

