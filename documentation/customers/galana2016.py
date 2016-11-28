import csv

from django.contrib.auth.models import User

from questions.models import Quiz, Sitting
from reviews.models import Review

quizzes = Quiz.objects.filter(id__in=[16, 17, 18])
sitting = Sitting.objects.get(pk=7)

with open('/srv/jibupro/documentation/customers/galana2016.csv', "rb") as ifile:
    reader = csv.reader(ifile)
    t = zip(reader)

for i in t:
    try:
        this_user = User.objects.get(email=i[0][0])
    except User.DoesNotExist:
        pass
    else:
        emails = [x.strip() for x in i[0][1].split(",")]
        reviewers = User.objects.filter(email__in=emails)
        for quiz in quizzes:
            this_review = Review(customer=quiz.customer, userprofile=this_user.userprofile, sitting=sitting, quiz=quiz)
            this_review.save()
            for person in reviewers:
                this_review.reviewers.add(person.userprofile)
