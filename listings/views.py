from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices


# This corresponds to the url views.index, views.listing and
# views.serach defined in the listings/urls.py file.

def index(request):
    """This is the default link for the listings app. See the btre_project/urls.py to see the links

        Args:
            request:The HTTP request
        Returns:
            render: call to render with the request and URL
        """
    # This will get of the listing objects that can be passed into our web page
    # Add an order by so that most recent listings are shown first.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # a dictionary can be used as an argument to pass information to the template or html page dynamically.
    # for example, if we define a dictionary that has a key of 'name', and a value (e.g. Dave) we can include that here
    # and then in the HTML file referenced (i.e. listings.html in this case) we can use {{ <key> }} notation to
    # dynamically populate this information.
    context = {
            'listings': paged_listings
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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
            'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    """Does a search for listings.

    Args:
        request:HTTP request object.
    Returns:
        render: call to render with listings.html URL
    """
    queryset_list = Listing.objects.order_by('-list_date')

    # Check if Keywords selection criteria was provided and if so filter results
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Check if city was included and filter results
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Check if state was included and filter results
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms will include up to the selected number of bedrooms
    # this could be adjusted to be exact if needed.
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms_cnt__gte=bedrooms)

    # Price will be up to and including
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
            'state_choices': state_choices,
            'price_choices': price_choices,
            'bedroom_choices': bedroom_choices,
            'listings': queryset_list,
            'values': request.GET
    }
    return render(request, 'listings/search.html', context)
