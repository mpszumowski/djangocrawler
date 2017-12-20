from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Countries


class SerializedView(APIView):
    def all_countries(self):
        countries = Countries.objects.all()
        return countries

    def get(self, request, format=None):
        serializer = CountrySerializer(self.all_countries(),
                                       many=True,
                                       context={"request": request})
        return Response(serializer.data)


class MainView(View):

    def get(self, request):
        countries = Countries.objects.order_by("name")
        return render(request, 'main.html', {'countries': countries})


# Create your views here.
