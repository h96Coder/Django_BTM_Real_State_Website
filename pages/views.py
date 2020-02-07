from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", \
              "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", \
              "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan"]
    bedrooms = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    prices = ['10000', '20000', '30000', '40000', '50000', '60000', '70000', '80000', '90000']
    context = {'states': states, 'bedrooms': bedrooms, 'prices': prices,'listings':listings}
    return render(request,'Pages/index.html',context)
def about(request):
    seller_of_month=Realtor.objects.filter(is_mvp=True)
    realtors =Realtor.objects.all()
    print(realtors,seller_of_month)
    context = {'realtors':realtors,'seller_of_month':seller_of_month,}
    return render(request,'Pages/about.html',context)
# Create your views here.
