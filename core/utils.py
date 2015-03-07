from django.contrib.auth.models import User

def fake_users(number=10):
    last_user = User.objects.order_by('-pk').first()
    for i in range(last_user.id+1, last_user.id+number):
        user_data = dict(first_name='User%dFirstName' % i,
                        last_name='User%dLastName' % i,
                        username='user%d' % i,
                        email='user%d@magendo.com' % i,
                        password='123456789',
                    )
        new_user = User.objects.create_user(**user_data)
    return "%s users created!" %number
