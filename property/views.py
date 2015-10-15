from django.http import HttpResponse
from django.shortcuts import render
from .models import House
from .forms import HouseForm


def add(request):
    """
    This view shows how we can create a new instance and save to database

    Every view must have request argument, which is passed by django
    """
    form = HouseForm()
    done = ''
    if request.POST:
        form = HouseForm(request.POST)
        if form.is_valid():
            house = House(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                address=form.cleaned_data['address'],
                bedrooms=form.cleaned_data['bedrooms'],
                bathrooms=form.cleaned_data['bathrooms'],
                kitchens=form.cleaned_data['kitchens']
            )
            house.save()
            done = 'Your form is submitted and saved.'

    return render(request, 'form.html', {'done': done, 'form': form})


def list(request):
    """
    This view list all houses
    """

    # get all house objects/rows stored in database
    houses = House.objects.all()

    # get only those added by above add view
    selected = House.objects.filter(title='This is added and also duplicated')
    return render(request, 'list.html', {
        'all_houses': houses,
        'selected_houses': selected
    })


def update(request):
    """
    update selected object
    """

    # get only those added by above add view
    house = House.objects.filter(title='This is added and also duplicated').first()
    house.title = house.title + ' and updated'
    house.save()

    # we will show list of house names
    return HttpResponse('done')
