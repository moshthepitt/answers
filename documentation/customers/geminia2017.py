import csv

from saas.models import Customer
from core import import_users


def import_geminia_users(filename, password, customer_id):
    """
    Takes Geminia formated csv and formats it to use core.import_users
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
