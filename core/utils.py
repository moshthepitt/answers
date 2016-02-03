from itertools import imap
import uuid
from datetime import datetime
import os

from django.template.defaultfilters import slugify
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
from django.conf import settings

from allauth.account.adapter import get_adapter
from sorl.thumbnail import get_thumbnail


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename
        if hasattr(instance, 'name') and instance.name:
            filename = '{}.{}'.format(slugify(instance.name[:255]), ext)
        elif hasattr(instance, 'title') and instance.title:
            filename = '{}.{}'.format(slugify(instance.title[:255]), ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(slugify(str(uuid.uuid4())), ext)
        # return the whole path to the file
        return os.path.join(self.path, "{}".format(datetime.now().year), "{}".format(datetime.now().month), filename)


def fake_users(number=10):
    last_id = 0
    last_user = User.objects.order_by('-pk').first()
    if last_user:
        last_id = last_user.id

    for i in range(last_id + 1, last_id + number):
        first_name = 'User{} FirstName'.format(i)
        last_name = 'User{} LastName'.format(i)
        email = 'user{}@example.com'.format(i)
        password = '123456789',

        unique_username = get_adapter().generate_unique_username([
            first_name,
            last_name,
            email,
        ])

        user_data = dict(first_name=first_name,
                         last_name=last_name,
                         username=unique_username,
                         email=email,
                         password=password,
                         )
        User.objects.create_user(**user_data)
    return "{} users created!".format(number)


def lists_overlap(a, b):
    sb = set(b)
    return any(imap(sb.__contains__, a))


def image_file(image, short_description='Image'):
    def image_thumb(self, obj):
        image = eval(image_thumb.image)
        if image:
            thumb = get_thumbnail(image.file, settings.ADMIN_THUMBS_SIZE)
            return u'<img width="{}" height={} src="{}" />'.format(thumb.width, thumb.height, thumb.url)
        else:
            return "No Image"

    image_thumb.__dict__.update({'short_description': short_description,
                                 'allow_tags': True,
                                 'image': image})
    return image_thumb
