from django.http import HttpResponse, Http404
from .models import Watershed,ffInfo,ManmadeFeature,NaturalFeature,Maintenance,FloraFauna,Observation
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    all_watershed = Watershed.objects.all()
    context = {
        'all_watershed': all_watershed
    }
    return render(request, 'watershed/index.html', context)


def detail(request, watershed_id):
        watershed = get_object_or_404(Watershed, pk=watershed_id)
        context = {
            'watershed': watershed
        }
        return render(request, 'watershed/detail.html', context)

class WatershedAdd(CreateView):
    model = Watershed
    fields = ['watershedID', 'name', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

