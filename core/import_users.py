import csv
from django.contrib.auth.models import User


def import_users(filename):
    """takes a csv with First Name, Last Name, Email and creates users"""
    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        t = zip(reader)
    import_list = [x[0] for x in t]
    for i, row in enumerate(import_list):
        data = dict(
            first_name=row[0].strip(),
            last_name=row[1].strip(),
            email=row[2].strip(),
            username=(row[0].strip().replace(" ", "") + row[1].strip().replace(" ", "") + str(i)).lower()
        )
        result = User(**data)
        result.save()
