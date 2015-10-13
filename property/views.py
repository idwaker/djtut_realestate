from django.http import HttpResponse
from .models import House


def add(request):
    """
    This view shows how we can create a new instance and save to database
    
    Every view must have request argument, which is passed by django
    """
    house = House(
        title='This is added and also duplicated',
        description="""This is duplicated because
        we don't have any field that is unique and everytime when someone
        calls this method a new object with the same attributes will be created
        and saved to database.""",
        price=128.78,
        address='This is address',
        bedrooms=3,
        bathrooms=2,
        kitchens=1
    )
    house.save()
    
    # this is view so it must return a response
    return HttpResponse('done')
