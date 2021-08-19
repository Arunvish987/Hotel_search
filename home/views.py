from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    amenities = Amenities.objects.all()
    context = {'amenities': amenities}
    return render(request, 'home/home.html', context)

def api_hotels(request):
    hotels_objs = Hotel.objects.all()

    price = request.GET.get('price')
    if price:
        hotels_objs = hotels_objs.filter(price__lte = price)

    amenities = request.GET.get('amenities')
    if amenities:
        amenities = amenities.split(',')
        am = []
        for a in amenities:
            try:
                am.append(int(e))
            except Exception as e:
                pass
        hotels_objs = hotels_objs.filter(amenities__in = am).distinct()
        
        
        

    payload = []
    for hotels_obj in hotels_objs:
        result = {}
        result['hotel_name'] = hotels_obj.hotel_name
        result['hotel_description'] = hotels_obj.hotel_description
        result['hotel_image'] = hotels_obj.hotel_image
        result['hotel_price'] = hotels_obj.price
        payload.append(result)

    return JsonResponse(payload, safe=False)
