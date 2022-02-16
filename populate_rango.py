import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    """ Creating a list of dictionaries."""

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/", "views": 32},
        {"title": "How to think like a computer scientist",
         "url": "http://www.greenteapress.com/thinkpython/", "views": 16},
        {"title": "Learn python in 10 minutes",
         "url": "http://www.korokithakis.net/tutorials/python/", "views": 8} ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01", "views": 32 },
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/", "views":16},
        {"title": "How to Tango with django",
         "url": "http://www.tangowithdjango.com", "views":8} ]

    other_pages = [ {"title":"Bottle",
                     "url":"http://bottlepy.org/docs/dev/", "views": 32},
                    {"title":"Flask",
                     "url":"http://flask.pocoo.org", "views": 16} ]

    cars = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views":32, "likes":16} }

    for car, car_data in cars.items():
        c = add_car(car, car_data["views"], car_data["likes"])
        for p in car_data["pages"]:
            add_page(c,p["title"], p["url"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(car, title, url, views=0):
    p = Page.objects.get_or_create(category=car, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_car(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

"""Execution is done here."""
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()