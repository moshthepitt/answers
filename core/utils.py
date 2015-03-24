from django.contrib.auth.models import User


def fake_users(number=10):
    last_id = 0
    last_user = User.objects.order_by('-pk').first()
    if last_user:
        last_id = last_user.id
    for i in range(last_id + 1, last_id + number):
        user_data = dict(first_name='User%dFirstName' % i,
                         last_name='User%dLastName' % i,
                         username='user%d' % i,
                         email='user%d@magendo.com' % i,
                         password='123456789',
                         )
        User.objects.create_user(**user_data)
    return "%s users created!" % number
