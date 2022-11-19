from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Users,Stores,Products,Transaction
import json,requests


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': 'latest_question_list'}
    # return render(request, 'index.html', context)
    return HttpResponse("region")#, content_type="application/json")


def tgmap(request):
    if request.method == 'GET':
      uid=request.GET['uid']
      lng=request.GET['lng']
      lat=request.GET['lat']
      # latest_question_list = Question.objects.
      region = json.loads(requests.get('https://api.mapbox.com/search/v1/reverse/69.1646,41.2217?access_token=pk.eyJ1Ijoic2VhcmNoLW1hY2hpbmUtdXNlci0xIiwiYSI6ImNrNnJ6bDdzdzA5cnAza3F4aTVwcWxqdWEifQ.RFF7CVFKrUsZVrJsFzhRvQ&language=en&country=UZ&limit=1&types=region').text)
      region=(region['features'][0]['properties']['description']).split(' ')[0]
      stores = Stores.objects.filter(region__contains=region)
      features = []

      for store in stores:
          features.append(
              {
              'type': 'Feature',
              'url': str(store.image_url),
              'properties': {
                  'message': str(store.sname),
                  'iconSize': [60, 60]
                              },
              'geometry': {
                  'type': 'Point',
                  'coordinates': [float(store.location_lang),float(store.location_lat)]
                  }
              }
              )
      context = {
          'features' : features,
          'lng' :lng,
          'lat' : lat,
          }
      return render(request, 'tgmap.html', context)
  
  
def products(request):

      context = {
          'products' : ['products','products']
          }
      return render(request, 'tgproducts.html', context) 