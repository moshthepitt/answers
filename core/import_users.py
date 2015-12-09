import csv
from django.contrib.auth.models import User

from allauth.account.adapter import get_adapter


def import_users(filename, password=None, customer=None):
    """takes a csv with First Name, Last Name, Email and creates users"""
    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        t = zip(reader)
    import_list = [x[0] for x in t]
    for i, row in enumerate(import_list):
        first_name = row[0].strip()
        last_name = row[1].strip()
        if not last_name:
            names = first_name.split(" ")
            if len(names) > 1:
                last_name = " ".join(names[1:])
                first_name = names[0]
        unique_username = get_adapter().generate_unique_username([
            first_name,
            last_name,
            row[2].strip(),
        ])
        data = dict(
            first_name=first_name,
            last_name=last_name,
            email=row[2].strip(),
            username=unique_username
        )
        result = User(**data)
        if password:
            result.set_password(password)
        result.save()
        if customer:
            result.userprofile.customer = customer
            result.userprofile.save()
