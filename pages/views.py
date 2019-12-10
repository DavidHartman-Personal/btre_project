from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    """This main view for the website.  It also shows up to 3 of the featured listings.

        Args:
            request:The HTTP request
        Returns:
            render: call to render with the request and URL
            """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # a dictionary can be used as an argument to pass information to the template or html page dynamically.
    context = {
            'listings': listings,
            'state_choices': state_choices,
            'price_choices': price_choices,
            'bedroom_choices': bedroom_choices,
    }
    # Pass in the context that contains the listing objects
    return render(request, 'pages/index.html', context)


def about(request):
    """The about page for the BT Realty site.  This view shows a list of all realtors and has a separate query and
    context object for the mvp/seller of the month.

            Args:
                request:The HTTP request
            Returns:
                render: call to render with the request and URL
                """
    realtors = Realtor.objects.order_by('-hire_date')

    # get the seller of the month -> is_mvp = True
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
            'realtors': realtors,
            'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)

