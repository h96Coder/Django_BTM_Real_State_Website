from django.shortcuts import render,get_object_or_404
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.http import HttpResponse
from .models import Listing
from .models import Realtor
def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listing=paginator.get_page(page)
   # print(a)
    context={
        'listings':paged_listing
    }
    return render(request,'Listings/listings.html',context)
def listing(request,listing_id):
    listing =get_object_or_404(Listing,pk =listing_id)
    seller_of_month = Realtor.objects.filter(is_mvp=True)[0]
    #print("ghfehfwhjfje",listing.bedrooms)
    context ={'listing':listing,'seller_of_month':seller_of_month}
    return render(request,'Listings/listing.html',context)
def search(request):
    queryset=Listing.objects.order_by('-list_date')
    querysets=Listing.objects.order_by('-list_date').filter(city="dxfcghbjk")
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", \
              "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", \
              "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan"]
    bedrooms = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    prices = ['10000', '20000', '30000', '40000', '50000', '60000', '70000', '80000', '90000']
    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querysets=queryset.filter(description__icontains=keywords);
    if "city" in request.GET:
        city = request.GET['city']
        if keywords:
            querysets|=queryset.filter(city=city);
    if "state" in request.GET:
        state = request.GET['state']
        print(state)
        if state:
            querysets|=queryset.filter(state=state);
    context={'listings':queryset}
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        #print(state)
        if bedrooms:
            querysets|=queryset.filter(bedrooms=bedrooms);
    context={'listings':queryset}
    if "price" in request.GET:
        price = request.GET['price']
        #print(state)
        if price:
            querysets|=queryset.filter(price=price);
    context={'states': states, 'bedrooms': bedrooms, 'prices': prices,'listings':querysets,'values':request.GET}
    print(queryset)
    return render(request,'Listings/search.html',context)