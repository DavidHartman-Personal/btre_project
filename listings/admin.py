from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    # Create a custom listing of the listings for the admin page.
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # makes the title as well as the ID hyperlink to the detailed page.
    list_display_links = ('id', 'title')
    # add a filter box on the right that can be used to filter the listings by realtor
    list_filter = ('realtor',)
    # Make the is_published field editable so that updates can be made from the listings page
    list_editable = ('is_published', )
    # Add search fields
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # add pagination, 25 per page
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)