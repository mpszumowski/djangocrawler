from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Countries
from scrapyd_api import ScrapydAPI


class SerializedView(APIView):
    def all_countries(self):
        countries = Countries.objects.all()
        return countries

    def get(self, request, format=None):
        serializer = CountrySerializer(self.all_countries(),
                                       many=True,
                                       context={"request": request})
        return Response(serializer.data)


class UpdateView(View):

    def get(self, request):
        # works only with scrapyd server launched
        scrapyd = ScrapydAPI('http://localhost:6800')
        countries_task = scrapyd.schedule('default', 'countries')
        food_task = scrapyd.schedule('default', 'food')
        pop_task = scrapyd.schedule('default', 'population')
        poverty_task = scrapyd.schedule('default', 'poverty')
        return JsonResponse({'countries_id': countries_task,
                             'food_id': food_task,
                             'population_id': pop_task,
                             'poverty_id': poverty_task,
                             'status': 'started'})
