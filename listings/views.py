from django.shortcuts import render
from django.http import HttpResponse

from .models import Listing


# This corresponds to the url views.index, views.listing and
# views.serach defined in the listings/urls.py file.

def index(request):
    # noinspection SpellCheckingInspection
    """This is the default link for the listings app. See the btre_project/urls.py to see the links

        Args:
            request:The HTTP request
        Returns:
            render: call to render with the request and URL
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


# Passing in listing_id to the listing request.
# This will add the listing.id value to the end of the URL
# e.g. http://127.0.0.1:8000/listings/1
# Chapter 7 - Display Listings in Template
def listing(request, listing_id):
    """
    Args:
        request:
        listing_id:
    Returns:
        render: call to render with listings.html URL
    """
    return render(request, 'listings/listing.html')


def search(request):
    """Does a search for listings.

    Args:
        request:HTTP request object.
    Returns:
        render: call to render with listings.html URL
    """
    return render(request, 'listings/search.html')
