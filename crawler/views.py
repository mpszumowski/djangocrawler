from django.shortcuts import render
from django.views import View
from .models import Countries


class MainView(View):

    def get(self, request):
        countries = Countries.objects.order_by("name")
        return render(request, 'main.html', {'countries': countries})


# Create your views here.
