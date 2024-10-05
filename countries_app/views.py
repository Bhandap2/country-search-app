# countries_app/views.py
from django.shortcuts import render
from .models import Country
from django.db.models import Q

def index(request):
    query = request.GET.get('q', '')
    if query:
        countries = Country.objects.filter(name__icontains=query)
    else:
        countries = Country.objects.all()
    return render(request, 'countries_app/index.html', {'countries': countries, 'query': query})
