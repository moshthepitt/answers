import csv

from django.contrib.auth.models import User

from saas.models import Customer
from users.utils import get_user_group
from core import import_users


def import_geminia_users(filename, password, customer_id):
    """
    Takes Geminia formated csv and formats it to use core.import_users

    Usage:
        from documentation.customers.geminia2017 import import_geminia_users

        filename = "example.csv"
        password = "Hunter2"
        customer_id = 6

        import_geminia_users(filename, password, customer_id)
    """
    try:
        this_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        pass
    else:
        with open(filename, "rb") as ifile:
            reader = csv.reader(ifile)
            t = zip(reader)
        import_list = [x[0] for x in t]
        export_list = []
        for i, row in enumerate(import_list):
            first_name = row[0].strip()
            last_name = row[1].strip()
            if not first_name:
                first_name = last_name.split()[0]
                last_name = " ".join(last_name.split()[1:])
            email = row[4].strip()
            export_list.append([first_name, last_name, email])
            export_filname = "/tmp/geminia-users.csv"
        with open(export_filname, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in export_list:
                writer.writerow(line)
        import_users.import_users(export_filname, password, this_customer)


def geminia_user_groups(filename, customer_id):
    """
    Creates use groups fro Geminia
    Usage:
        from documentation.customers.geminia2017 import geminia_user_groups

        filename = "example.csv"
        customer_id = 6

        geminia_user_groups(filename, customer_id)
    """
    try:
        this_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        pass
    else:
        with open(filename, "rb") as ifile:
            reader = csv.reader(ifile)
            t = zip(reader)
        import_list = [x[0] for x in t]
        for row in import_list:
            email = row[4].strip()
            this_user = User.objects.filter(
                userprofile__customer=this_customer, email=email).first()
            if this_user:
                dept = row[2].strip()
                user_group = get_user_group(dept, this_customer)
                this_user.userprofile.group.add(user_group)


def geminia_managers(filename, customer_id):
    """
    Quickly assign managers to existing staff
    Usage:
        from documentation.customers.geminia2017 import geminia_managers

        filename = "example.csv"
        customer_id = 6

        geminia_managers(filename, customer_id)
    """
    try:
        this_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        pass
    else:
        with open(filename, "rb") as ifile:
            reader = csv.reader(ifile)
            t = zip(reader)

        import_list = [x[0] for x in t]

        for row in import_list:
            email = row[4].strip()
            this_user = User.objects.filter(
                userprofile__customer=this_customer, email=email).first()
            if this_user:
                supervisor_email = row[5].strip()
                this_supervisor = User.objects.filter(
                    userprofile__customer=this_customer,
                    email=supervisor_email).first()
                if this_supervisor:
                    this_user.userprofile.manager = this_supervisor.userprofile
                    this_user.userprofile.save()
