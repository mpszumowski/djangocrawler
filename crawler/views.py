from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Countries
from scrapyd_api import ScrapydAPI


class SerializedView(APIView):

    def get(self, request, format=None):
        serializer = CountrySerializer(Countries.all_countries(),
                                       many=True,
                                       context={"request": request})
        return Response(serializer.data)


class UpdateView(View):

    def post(self, request):
        # works only with scrapyd server launched
        scrapyd = ScrapydAPI('http://localhost:6800')
        # launches the scrapers
        countries_task = scrapyd.schedule('default', 'countries')
        food_task = scrapyd.schedule('default', 'food')
        pop_task = scrapyd.schedule('default', 'population')
        poverty_task = scrapyd.schedule('default', 'poverty')
        # returns the unique id's of each scheduled task
        return JsonResponse({'countries_id': countries_task,
                             'food_id': food_task,
                             'population_id': pop_task,
                             'poverty_id': poverty_task})

    def get(self, request):
        scrapyd = ScrapydAPI('http://localhost:6800')
        # receives the id's of each task
        countries_id = request.GET.get('countries_id', None)
        food_id = request.GET.get('food_id', None)
        population_id = request.GET.get('population_id', None)
        poverty_id = request.GET.get('poverty_id', None)
        # determine the status of each task and return dict
        jobs = {'countries_status':
                    scrapyd.job_status('default', countries_id),
                'food_status':
                    scrapyd.job_status('default', food_id),
                'population_status':
                    scrapyd.job_status('default', population_id),
                'poverty_status':
                    scrapyd.job_status('default', poverty_id)}
        return JsonResponse(jobs)
