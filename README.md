# Django starter template
A little something-something that I use as my starter template for personal and commercial Django projects.  The basic idea is to save time when starting Django projects - at the beginning of all Django projects I found I always did certain things every single time.

This starter template gives me the opportunity to as quickly as possible get through the boilerplate and start real & interesting work on new DJango projects.

# What is included
* A base html template based on Bootstrap
* A simple home page view and template (core.views)
* Bootstrap static files
* A simple method to create fake/dummy users (core.utils.fake_users)
* A UserProfile model that extends django.contrib.auth.models.User
* A context processor to make the site name available to templates (core.context_processors.site_processor)
* Django flatpages set app with a wysiwyg editor (Redactor)
* Django Allauth templates set up to work with Bootstrap and django-crispy-forms

# Installed Third Party Apps
* django-suit
* django-suit-redactor
* django-allauth
* django-debug-toolbar
* django-crispy-forms
* django-pagination
* django-compressor
* django-cacheops

# Installation
1. Download or git clone the project
2. Have a look at template.local_settings.py to make configuarion changes as you need.  It would be a good idea to add local_settings.py to gitignore so that this file is not tracked by Git.
3. Run server
4. ??
5. Profit
