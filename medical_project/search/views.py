from django.shortcuts import render, HttpResponse
from .models import Medicine
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
class HomePage(TemplateView):
    template_name = 'homepage.html'

class DetailsPage(TemplateView):
    template_name = 'contact.html'


def search_med(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multi_search = Q(Q(sku_name__icontains=q) | Q(salt_name__icontains=q))      
        all_meds = Medicine.objects.filter(multi_search)

    else:
        all_meds = Medicine.objects.all()

    dict_meds = {'all_meds' : all_meds}

    return render(request, 'search/result.html',dict_meds )