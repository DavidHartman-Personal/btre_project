from django.shortcuts import render
from django.http import HttpResponse

from .models import Listing
# This corresponds to the url views.index, views.listing and
# views.serach defined in the listings/urls.py file.

def index(request):
    """This is the default link for the listings app.  See the btre_project/urls.py to see the links
    """
    # This will get of the listing objects that can be passed into our web page
    listings = Listing.objects.all()
    # a dictionary can be used as an argument to pass information to the template or html page dynamically.
    # for example, if we define a dictionary that has a key of 'name', and a value (e.g. Dave) we can include that here
    # and then in the HTML file referenced (i.e. listings.html in this case) we can use {{ <key> }} notation to
    # dynamically populate this information.
    context = {
            'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

