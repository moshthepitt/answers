import csv

from django.contrib.auth.models import User

from questions.models import Quiz, Sitting
from reviews.models import Review

quizzes = Quiz.objects.filter(id__in=[29])
sitting = Sitting.objects.get(pk=11)

# peer reviews
with open('/home/mosh/Desktop/galana2017.csv',
          "rb") as ifile:
    reader = csv.reader(ifile)
    t = zip(reader)

for i in t:
    try:
        this_user = User.objects.get(email=i[0][0])
    except User.DoesNotExist:
        print(i[0][0])
    else:
        emails = [x.strip() for x in i[0][1].split(",")]
        reviewers = User.objects.filter(email__in=emails)
        for quiz in quizzes:
            this_review = Review(customer=quiz.customer,
                                 userprofile=this_user.userprofile,
                                 sitting=sitting, quiz=quiz)
            this_review.save()
            for person in reviewers:
                this_review.reviewers.add(person.userprofile)
            groups = this_user.userprofile.group.all()
            for group in groups:
                if group.manager:
                    this_review.reviewers.add(group.manager)
